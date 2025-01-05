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

    // Function to add a node in beginning of linked list
    public void addFirst (int item)
    {
        // Create a temp node which points to head
        Node temp = new Node (item, head);

        // If linked list is empty, temp is the head and tail node both
        if (this.size == 0)
        {
            this.head = this.tail = temp;
        }

        // else set the head such that it now points to temp node
        else
        {
            this.head = temp;
        }
        this.size++;
    }

    public boolean isPalindrome ()
    {
        HeapMover start = new HeapMover ();
        start.node = this.head;
        return this.isPalindrome (start, this.head, 0);
    }

    //Function to check whether linked list is palindrome or not
    private boolean isPalindrome (HeapMover start, Node end, int floor)
    {
        //Base case is when we reach end of linked list
        if (end == null)
        {
            return true;
        }

        //Recursive calls
        boolean rv = this.isPalindrome (start, end.next, floor + 1);

        //If any recursive call results in false then return false
        if (rv == false)
        {
            return false;
        }

        //Till floor is greater than 1/2 * size of linked list
        if (floor >= this.size () / 2)
        {
            //If data of start node and end node is not same then it is not palindrome
            if (start.node.data != end.data)
            {
                return false;
            }

            //Change start node so that it now points to the next node
            else
            {
                start.node = start.node.next;
                return true;
            }
        }
        return rv;
    }

    //Class to keep a node in the heap
    private class HeapMover
    {
        Node node;
    }
}