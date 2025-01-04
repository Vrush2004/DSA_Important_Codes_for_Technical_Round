package LinkedList.SinglyLinkedList;

public class FindMiddle {
    Node head;
    // not using parameterized constructor would by default
    // force head instance to become null
    // Node head = null;  // can also do this, but not required

    // Node Class
    class Node
    {
        int data;
        Node next;

        Node (int x)		// parameterized constructor
        {
        data = x;
        next = null;
        }
    }
    public Node insert (int data)
    {
        // Creating newNode memory & assigning data value
        Node newNode = new Node (data);
        // assigning this newNode's next as current head node
        newNode.next = head;

        // re-assigning head to this newNode
        head = newNode;

        return head;
    }

    public void display ()
    {
        Node node = head;
        //as linked list will end when Node reaches Null
        while (node != null)
        {
            System.out.print (node.data + " ");
            node = node.next;
        }
        System.out.println ();
    }

    public int mid ()
    {
        return this.midNode ().data;
    }

    //Function to find the mid node
    private Node midNode ()
    {
        //Take two pointers p1 and p2
        Node p1 = this.head;
        Node p2 = this.head;

        //Move p1 by one node and p2 by two nodes
        while (p2.next != null && p2.next.next != null)
        {
            p1 = p1.next;
            p2 = p2.next.next;
        }
        //When p2 reaches the end, p1 will point to the mid node
        return p1;
    }
    public static void main (String args[])
    {
        FindMiddle ll = new FindMiddle ();

        ll.insert (6);
        ll.insert (5);
        ll.insert (3);
        ll.insert (4);
        ll.insert (2);

        ll.display ();

        System.out.println ("Middle of the linked list is :- ");
        System.out.println (ll.mid ());
    }
}