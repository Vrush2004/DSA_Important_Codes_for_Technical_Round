#include <iostream>
#include <queue>
#include <vector>
#include <cstdlib>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 * 
 * typedef struct ListNode listnode;
 * 
 * listnode* listnode_new(int val) {
 *     listnode* node = (listnode *) malloc(sizeof(listnode));
 *     node->val = val;
 *     node->next = NULL;
 *     return node;
 * }
 */

// Custom comparator to compare nodes based on their value
struct Compare {
    bool operator()(listnode* a, listnode* b) {
        return a->val > b->val;  // Min-heap based on value
    }
};

listnode* mergeKLists(listnode** A, int n1) {
    // Create a min-heap (priority queue)
    priority_queue<listnode*, vector<listnode*>, Compare> minHeap;

    // Push the head of each linked list into the heap
    for (int i = 0; i < n1; i++) {
        if (A[i] != NULL) {
            minHeap.push(A[i]);
        }
    }

    listnode* head = NULL;  // Head of the merged list
    listnode* tail = NULL;  // Tail of the merged list

    // Process the heap
    while (!minHeap.empty()) {
        // Get the smallest node from the heap
        listnode* node = minHeap.top();
        minHeap.pop();

        // Add it to the merged list
        if (head == NULL) {
            head = node;  // First node in the merged list
            tail = head;  // Tail points to head
        } else {
            tail->next = node;
            tail = tail->next;  // Move the tail pointer
        }

        // If the current node has a next node, push it into the heap
        if (node->next != NULL) {
            minHeap.push(node->next);
        }
    }

    return head;  // Return the head of the merged sorted list
}
}
