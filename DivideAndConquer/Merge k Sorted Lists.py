# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For debugging, convert linked list to list
    def to_list(self):
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Min-Heap to store (value, index, node)
        min_heap = []
        
        # Initialize heap with head nodes of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        # Dummy node to help in building the result list
        dummy = ListNode(0)
        current = dummy

        while min_heap:
            # Extract the smallest node
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = node  # Move forward in the result list

            # Push the next node from the same list if available
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next  # Return the merged linked list head