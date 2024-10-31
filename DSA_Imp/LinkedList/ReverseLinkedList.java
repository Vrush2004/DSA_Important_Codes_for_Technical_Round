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
        head = reverse(head);
        print(head);
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