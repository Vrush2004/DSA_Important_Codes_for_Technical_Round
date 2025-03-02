# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before `left`
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversing
        current = prev.next
        next_node = None
        
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next