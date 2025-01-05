package LinkedList.DoublyLinkedList;

public class InsertionAtBeginning {
    Node head;
    // not using parameterized constructor would by default
    // force head instance to become null
    // Node head = null; // can also do this, but not required

    // Node Class
    class Node
    {
        int data;
        Node next, prev;

        Node (int x)		// parameterized constructor
        {
            data = x;
            next = null;
            prev = null;
        }
    }

    public void insertBeginning (int data)
    {
        // Creating newNode memory & assigning data value
        Node freshNode = new Node (data);

        freshNode.next = head;
        freshNode.prev = null;

        // if DLL had already >=1 nodes
        if (head != null)
            head.prev = freshNode;

        // changing head to this
        head = freshNode;
    }

    public void printList ()
    {
        Node node = head;
        Node end = null;
        //as linked list will end when Node reaches Null

        System.out.print ("\nIn forward: ");
        while (node != null)
        {
            System.out.print (node.data + " ");
            end = node;
            node = node.next;
        }
        System.out.print ("\nIn backward: ");

        while (end != null)
        {
            System.out.print (end.data + " ");
            end = end.prev;
        }
        System.out.println ();
    }

    public static void main (String args[])
    {
        InsertionAtBeginning doublylist = new InsertionAtBeginning ();

        doublylist.insertBeginning (3);
        doublylist.insertBeginning (2);
        doublylist.insertBeginning (1);
        doublylist.insertBeginning (4);
        doublylist.insertBeginning (5);

        doublylist.printList ();
    }
}