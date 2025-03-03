# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque([root])  # Start BFS with root node

        while queue:
            size = len(queue)
            prev = None  # Tracks the previous node in the level
            
            for _ in range(size):
                node = queue.popleft()
                
                if prev:
                    prev.next = node  # Link previous node to current node
                
                prev = node  # Update previous node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            prev.next = None  # Last node of each level should point to NULL

        return root