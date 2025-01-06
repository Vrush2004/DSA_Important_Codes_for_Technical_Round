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
 * @input A : Head pointer of linked list 
 * 
 * @Output head pointer of list.
 */
listnode* reverseList(listnode* A) {
    listnode* prev = NULL;  // Initially, the previous node is NULL
    listnode* curr = A;     // Start with the head node
    listnode* next = NULL;  // Temporary pointer to store the next node
    
    // Traverse the list and reverse the links
    while (curr != NULL) {
        next = curr->next;     // Store the next node
        curr->next = prev;     // Reverse the current node's pointer
        prev = curr;           // Move prev forward
        curr = next;           // Move curr forward
    }
    
    // When the loop ends, prev will be pointing to the new head of the reversed list
    return prev;
}