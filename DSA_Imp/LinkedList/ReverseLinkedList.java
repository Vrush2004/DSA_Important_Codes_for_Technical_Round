// Given the head of singly linkedlist. Reverse the linkedlist in single traversal.
// sample input 
// 1 -> 2 -> 3 -> 4 -> 5 -> NULL
// sample output
// 5 -> 4 -> 3 -> 2 -> 1 -> NULL
// time complexity = O(n)
// space complexity = O(1)

package DSA_Imp.LinkedList;

import java.util.Scanner;

class ListNode{
    public int val;
    public ListNode next;
    ListNode(int x){
        val = x;
        next = null;
    }
}
public class ReverseLinkedList {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the number of nodes:");
        int n = scanner.nextInt();
        
        if (n <= 0) {
            System.out.println("Linked list is empty.");
            return;
        }
        
        System.out.println("Enter the values of the nodes:");
        ListNode head = new ListNode(scanner.nextInt());
        ListNode current = head;
        
        for (int i = 1; i < n; i++) {
            current.next = new ListNode(scanner.nextInt());
            current = current.next;
        }
        
        System.out.println("Original Linked List:");
        print(head);

        // Reversing the linked list
        head = reverse(head);

        System.out.println("Reversed Linked List:");
        print(head);

        scanner.close();
    }

    public static void print(ListNode head){
        ListNode temp = head;
        while (temp != null) {
            System.out.println(temp.val + " ");
            temp = temp.next;
        }
    }

    public static ListNode reverse(ListNode head){
        ListNode prev = null;
        ListNode curr = head;

        while(curr != null){
            ListNode next = curr.next;
            curr.next = prev;

            // move prev and curr
            prev = curr;
            curr = next;
        }
        return prev;
    }
}