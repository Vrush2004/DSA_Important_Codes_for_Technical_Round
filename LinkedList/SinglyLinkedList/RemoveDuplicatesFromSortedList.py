# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)  
        prev = dummy  

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next  
            else:
                prev = prev.next  

            head = head.next 

        return dummy.next