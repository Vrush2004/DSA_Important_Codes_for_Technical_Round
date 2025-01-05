package LinkedList.SinglyLinkedList;

public class LinkedListIsPalindrome {
    public static void main (String[]args) throws Exception
    {
        LinkedListIsPalindrome ll = new LinkedListIsPalindrome ();
        ll.addFirst (10);
        ll.addFirst (20);
        ll.addFirst (30);
        ll.addFirst (40);
        ll.addFirst (40);
        ll.addFirst (30);
        ll.addFirst (20);
        ll.addFirst (10);

        ll.display ();

        System.out.println (ll.isPalindrome ());
    }

    private class Node
    {
        int data;
        Node next;

        // Node constructor
        // There are two fields in the node- data and address of next node
        public Node (int data, Node next)
        {
            this.data = data;
            this.next = next;
        }
    }

    private Node head;
    private Node tail;
    private int size;

    // Linked list constructor
    public LinkedListIsPalindrome ()
    {
        this.head = null;
        this.tail = null;
        this.size = 0;

    }

    // Function to find the size of linked list
    public int size ()
    {
        return this.size;
    }

    // Function to check whether linked list is empty or not
    public boolean isEmpty ()
    {
        return this.size () == 0;
    }

    // Function to traverse and print the linked list
    public void display ()
    {
        Node temp = head;
        while (temp != null)
        {
            System.out.print (temp.data + "  ");
            temp = temp.next;
        }
        System.out.println ("END");
    }
}