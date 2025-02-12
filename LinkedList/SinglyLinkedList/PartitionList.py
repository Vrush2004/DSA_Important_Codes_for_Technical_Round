# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to track the smaller and greater partitions
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers for building the two lists
        smaller = smaller_head
        greater = greater_head
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                smaller.next = current
                smaller = smaller.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Connect the smaller list with the greater list
        greater.next = None  # End the greater list
        smaller.next = greater_head.next  # Merge the two lists
        
        return smaller_head.next  # Return the head of the new list