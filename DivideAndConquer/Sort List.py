# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Base case: empty or single-node list is already sorted
        
        # Step 1: Find the middle of the list
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None  # Break the list into two halves
        
        # Step 2: Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def getMid(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow  # Middle node found

    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to simplify merging
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next  # Move the pointer forward
        
        # Attach the remaining elements
        tail.next = list1 if list1 else list2
        
        return dummy.next  # Return sorted list starting from next of dummy
