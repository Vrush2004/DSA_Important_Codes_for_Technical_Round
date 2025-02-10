# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create new nodes and insert them next to the original nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next  # Move to the next original node

        # Step 2: Assign the correct random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next  # Copy the random pointer
            curr = curr.next.next  # Move to the next original node

        # Step 3: Separate the copied list from the original list
        curr = head
        copied_head = head.next
        copied_curr = copied_head

        while curr:
            curr.next = curr.next.next  # Restore original list
            copied_curr.next = copied_curr.next.next if copied_curr.next else None  # Link copied nodes
            curr = curr.next
            copied_curr = copied_curr.next
        
        return copied_head