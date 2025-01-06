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

// Function to print a linked list
void printList(listnode* head) {
    while (head != NULL) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

// Helper function to create a new linked list node
listnode* listnode_new(int val) {
    listnode* node = new listnode();
    node->val = val;
    node->next = NULL;
    return node;
}

int main() {
    // Example 1:
    listnode* list1 = listnode_new(1);
    list1->next = listnode_new(10);
    list1->next->next = listnode_new(20);

    listnode* list2 = listnode_new(4);
    list2->next = listnode_new(11);
    list2->next->next = listnode_new(13);

    listnode* list3 = listnode_new(3);
    list3->next = listnode_new(8);
    list3->next->next = listnode_new(9);

    listnode* lists[] = {list1, list2, list3};
    listnode* result = mergeKLists(lists, 3);
    printList(result);

    // Example 2:
    listnode* list4 = listnode_new(10);
    list4->next = listnode_new(12);

    listnode* list5 = listnode_new(13);

    listnode* list6 = listnode_new(5);
    list6->next = listnode_new(6);

    listnode* lists2[] = {list4, list5, list6};
    listnode* result2 = mergeKLists(lists2, 3);
    printList(result2);

    return 0;
}
