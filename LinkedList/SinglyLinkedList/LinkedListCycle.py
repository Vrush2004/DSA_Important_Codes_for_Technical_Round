# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head  # Both pointers start at the head
        
        while fast and fast.next:  # Ensure fast does not reach None
            slow = slow.next  # Move slow by one step
            fast = fast.next.next  # Move fast by two steps
            
            if slow == fast:  # If both meet, cycle detected
                return True
        
        return False  # If fast reaches None, no cycle exists