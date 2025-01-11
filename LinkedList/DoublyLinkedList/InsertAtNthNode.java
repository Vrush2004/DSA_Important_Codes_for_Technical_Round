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

    public void insertBeginning(int data) {
        // Creating newNode memory & assigning data value
        Node freshNode = new Node(data);

        freshNode.next = head;
        freshNode.prev = null;

        // if DLL had already >=1 nodes
        if (head != null)
            head.prev = freshNode;

        // changing head to this
        head = freshNode;
    }

    public void insertEnd(int data) {
        // Creating newNode memory & assigning data value
        Node freshNode = new Node(data);

        // assign data
        // since this will be the last node its next will be NULL
        freshNode.next = null;

        //if we are entering the first node
        if (head == null) {
            head = freshNode;
            freshNode.prev = null;
            return;
        }

        Node last = head;

        // traverse to the current last node
        while (last.next != null)
            last = last.next;

        // assign current last node's next to this new node
        // assign new node's previous to this last node
        last.next = freshNode;
        freshNode.prev = last;
        // new_node becomes the last node now

    }

    public static void main(String args[])
    {
        InsertAtNthNode doublylist = new InsertAtNthNode();

        doublylist.insertBeginning(3);
        doublylist.insertBeginning(2);
        doublylist.insertBeginning(1);
        doublylist.insertBeginning(4);
        doublylist.insertBeginning(7);

        //Inserts after 4th position
        doublylist.insertAfterPosition(4,5);

        doublylist.printList();
    }
}