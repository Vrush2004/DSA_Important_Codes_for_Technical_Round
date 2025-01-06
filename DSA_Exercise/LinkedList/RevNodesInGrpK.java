// Give a linkedlist. Reverse every k nodes of the given linkedlist. If the number of nodes is not a multiple of k then left out nodes, in the end, should remain as it is.
// Sample input 
// 1 2 3 4 5 6 7 8 null
// k = 3
// sample output
// 3 2 1 6 5 4 7 8 null
// time complexity = O(n)
// space complexity = O(1)

package DSA_Exercise.LinkedList;

import java.util.Scanner;

class ListNode {
    public int val;
    public ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class RevNodesInGrpK {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        ListNode head = new ListNode(scn.nextInt());
        ListNode temp = head;
        ListNode temp1 = head, temp2 = head;
        while(n-- > 1){
            temp.next = new ListNode(scn.nextInt());
            temp = temp.next;
            if(n==4){
                temp1 = temp;
            }
            temp2 = temp;
        }
        temp2.next = temp1;
        head = kReverse(head, scn.nextInt());
        print(head);
    }

    public static ListNode kReverse(ListNode head, int k) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode pointer = dummy;

        while (pointer.next != null) {
            // Check if there are k nodes available
            ListNode node = pointer;
            for (int i = 0; i < k && node != null; i++) {
                node = node.next;
            }
            if (node == null) {
                // Less than k nodes available
                break;
            }

            // Reverse k nodes
            ListNode prev = null, curr = pointer.next;
            for (int i = 0; i < k; i++) {
                ListNode next = curr.next;
                curr.next = prev;
                prev = curr;
                curr = next;
            }

            // Reconnect the reversed part with the rest of the list
            ListNode tail = pointer.next;
            pointer.next = prev;
            tail.next = curr;
            pointer = tail;
        }
        return dummy.next;
    }

    public static void print(ListNode head){
        ListNode temp = head;
        while (temp != null) {
            System.out.println(temp.val + " ");
            temp = temp.next;
        }
    }
}