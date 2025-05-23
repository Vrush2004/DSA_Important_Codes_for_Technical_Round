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

    public void insertAfterPosition(int n, int data) {
        int len = getLength(head);

        // if insertion position is 0 means entering at start
        if (n == 0) {
            insertBeginning(data);
            return;
        }
        // means inserting after last item
        if (n == len) {
            insertEnd(data);
            return;
        }

        // else insertion will happen somewhere in the middle


        if (n < 1 || len < n) System.out.println("Invalid position");
        else { Node freshNode = new Node(data);
            // can remove null assignments also (constructor takes care of these)
            // added just for explanation purpose

            freshNode.next = null;

            freshNode.prev = null;
            // nthNode used to traverse the Linked List

            Node nthNode = head;

            // traverse till the nth node

            while (--n > 0) {
                nthNode = nthNode.next;
            }

            Node nextNode = nthNode.next; // (n+1)th node

            // assigning (n+1)th node's previous to this new node
            nextNode.prev = freshNode;

            // new_node's next assigned to (n+1)th node
            freshNode.next = nextNode;
            // new_node's previous assigned to nth node
            freshNode.prev = nthNode;

            // assign nth node's next to new_node
            nthNode.next = freshNode;
        }
    }

    public void printList() {
        Node node = head;
        Node end = null;
        //as linked list will end when Node reaches Null

        System.out.print("\nIn forward: ");
        while (node != null) {
            System.out.print(node.data + " ");
            end = node;
            node = node.next;
        }
        System.out.print("\nIn backward: ");

        while (end != null) {
            System.out.print(end.data + " ");
            end = end.prev;
        }
        System.out.println();
    }

    // required for insertPosition() method
    public int getLength(Node node) {
        int size = 0;
        // traverse to the last node each time incrementing the size
        while (node != null) {
            node = node.next;
            size++;
        }
        return size;
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