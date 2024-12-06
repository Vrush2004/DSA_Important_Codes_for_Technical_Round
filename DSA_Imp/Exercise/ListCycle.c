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

/**
 * Detect the cycle in the linked list and return the node where the cycle starts.
 * @input A : Head pointer of the linked list.
 * @output Return the node where the cycle begins, or NULL if no cycle exists.
 */
listnode* detectCycle(listnode* A) {
    if (A == NULL || A->next == NULL) {
        return NULL;
    }

    listnode *slow = A, *fast = A;

    // Step 1: Detect if there's a cycle using the tortoise and hare method.
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;             // Move slow pointer one step
        fast = fast->next->next;       // Move fast pointer two steps

        // If slow and fast pointers meet, a cycle is detected
        if (slow == fast) {
            // Step 2: Find the start of the cycle.
            slow = A;  // Reset slow pointer to the head
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;  // Return the node where the cycle starts
        }
    }

    // If no cycle is found, return NULL
    return NULL;
}