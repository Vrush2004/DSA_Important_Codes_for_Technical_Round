// Give a linkedlist. Determine if the linkedlist has a cycle in it.
// time complexity = O(n)
// space complexity = O(1)

package DSA_Imp.LinkedList;
import java.util.*;

class ListNode{
    public int val;
    public ListNode next;
    ListNode(int x){
        val = x;
        next = null;
    }
}

public class DetectCycleInLL {
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
        // temp2.next = temp1;
        System.out.println(hasCycle(head));
    }

    public static boolean hasCycle(ListNode head){
        ListNode slow = head, fast = head;
        while(fast != null && fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                return true;
            }
        }
        return false;
    }
}