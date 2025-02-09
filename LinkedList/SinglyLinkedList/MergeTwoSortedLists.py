# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        current = dummy  # Pointer to track the last node in the merged list

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:  # Take the smaller value node
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next  # Move to the newly added node

        # If any elements are left in either list, attach them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next  # Return the merged list starting from the first real node