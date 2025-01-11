package LinkedList.DoublyLinkedList;
import java.lang.*;

class InsertAtNthNode {
    Node head;
    // not using parameterized constructor would by default
    // force head instance to become null
    // Node head = null;  // can also do this, but not required

    // Node Class
    class Node {
        int data;
        Node next, prev;

        Node(int x) // parameterized constructor
        {
            data = x;
            next = null;
            prev = null;
        }
    }
}