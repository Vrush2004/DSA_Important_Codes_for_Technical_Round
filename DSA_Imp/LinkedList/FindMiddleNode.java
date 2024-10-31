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
        System.out.println(middleNode(head));
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