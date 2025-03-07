package LinkedList.SinglyLinkedList;

public class ReverseLinkedList {
    Node head;

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

    public void display ()
    {
        Node temp = head;
        while (temp != null)
        {
            System.out.print (temp.data + " ");
            // Set temp to point to the next node
            temp = temp.next;
        }
        System.out.println ("END");
    }

    public Node insertBeginning (int data)
    {
        Node newNode = new Node (data);
        newNode.next = head;
        head = newNode;

        return head;
    }
    public void reverse ()
    {
        Node pointer = head;
        Node previous = null, current = null;

        while (pointer != null)
        {
            current = pointer;
            pointer = pointer.next;

            // reverse the link
            current.next = previous;
            previous = current;
            head = current;
        }

    }

    public static void main (String[]args)
    {
        try
        {
            ReverseLinkedList ll = new ReverseLinkedList ();
            ll.insertBeginning (2);
            ll.insertBeginning (4);
            ll.insertBeginning (6);
            ll.insertBeginning (8);
            
            System.out.println("LinkedList before reversal : ");

            ll.display ();
            
            System.out.println("LinkedList after reversal : ");

            ll.reverse ();
            ll.display ();
        }
        catch (Exception e)
        {
        System.out.println ("Exception occurred.");
        }
    }
}