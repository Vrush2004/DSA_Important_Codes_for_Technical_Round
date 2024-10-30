// Give head of a linkedlist. Find the middle node.
// Sample input 
// 10 - 12 - 23 - 2 - 15- 9 - 6 - 21 - null
// sample output 
// 2
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

public class FindMiddleNode {
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

        int middleValue = middleNode(head);
        System.out.println("The middle node value is: " + middleValue);

        scanner.close();
    }

    public static int middleNode(ListNode head){
        ListNode slow = head;
        ListNode fast = head;

        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow.val;
    }
}