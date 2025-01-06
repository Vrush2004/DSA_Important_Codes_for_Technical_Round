/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

ListNode* Solution::solve(ListNode* A) {
    // Handle case when the list is empty or has only one node
    if (A == NULL || A->next == NULL) {
        return NULL;
    }

    ListNode *slow = A, *fast = A, *prev = NULL;

    // Move fast pointer 2 steps and slow pointer 1 step until fast reaches the end
    while (fast != NULL && fast->next != NULL) {
        prev = slow;           // Keep track of the previous node to slow
        slow = slow->next;     // Move slow pointer 1 step
        fast = fast->next->next; // Move fast pointer 2 steps
    }

    // Now slow is at the middle node, prev is at the node before slow
    if (prev != NULL) {
        prev->next = slow->next; // Skip the middle node
    }

    // Return the modified list
    return A;
}