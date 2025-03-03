# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Check if there are at least k nodes
        temp = head
        count = 0
        while temp and count < k:
            temp = temp.next
            count += 1

        # If there are at least k nodes, proceed with reversal
        if count == k:
            prev = None
            curr = head
            next_node = None
            
            # Reverse k nodes
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Recursively call for the next k nodes
            head.next = self.reverseKGroup(curr, k)
            
            return prev  # New head after reversing k nodes
        
        return head  # Return head if fewer than k nodes are left

# Helper function to create a linked list from a list
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
sol = Solution()
head = create_list([1,2,3,4,5])
k = 2
new_head = sol.reverseKGroup(head, k)
print_list(new_head)  # Output: 2 -> 1 -> 4 -> 3 -> 5 -> None

head = create_list([1,2,3,4,5])
k = 3
new_head = sol.reverseKGroup(head, k)
print_list(new_head)  # Output: 3 -> 2 -> 1 -> 4 -> 5 -> None