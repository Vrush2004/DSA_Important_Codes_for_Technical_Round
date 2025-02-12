# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize k
        k = k % length
        if k == 0:
            return head  # No rotation needed

        # Step 3: Find new tail (length - k - 1) and new head (length - k)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # Break the link

        # Step 4: Connect old tail to old head
        tail.next = head

        return new_head