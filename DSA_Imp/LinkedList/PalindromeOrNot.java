// Give a singly linkedlist. Determine if it is a palindrome.
// sample input 
// 1 2 3 2 1
// sample output
// true
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

public class PalindromeOrNot {
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
        System.out.println(isPalindrome(head));
    }

    public static void print(ListNode head){
        ListNode temp = head;
        while (temp != null) {
            System.out.println(temp.val + " ");
            temp = temp.next;
        }
    }
}