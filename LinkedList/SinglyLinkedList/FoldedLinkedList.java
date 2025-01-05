package LinkedList.SinglyLinkedList;

public class FoldedLinkedList {
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

    public void foldLinkedList (Node head)
    {
        Node slowPointer = head;
        Node fastPointer = head;
        while (fastPointer != null)
        {
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next;
            if (fastPointer != null)
                fastPointer = fastPointer.next;
        }
        Node middlePointer = slowPointer;
        Node reverseLastHalf = reverseLinkedList (slowPointer);
        while (reverseLastHalf != null && head != middlePointer)
        {
            Node tempHead = head.next;
            Node tempReverse = reverseLastHalf.next;
            reverseLastHalf.next = head.next;
            head.next = reverseLastHalf;
            head = tempHead;
            reverseLastHalf = tempReverse;
        }
        if (reverseLastHalf != null)
            reverseLastHalf.next = null;
        else
            head.next = null;
    }

    public static Node reverseLinkedList (Node head)
    {
        if (head.next == null)
            return head;
        Node newHead = reverseLinkedList (head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }

    public Node insert (int data)
    {
        Node newNode = new Node (data);
        newNode.next = head;
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
        System.out.println ("\n");
    }
    public static void main (String args[])
    {
        FoldedLinkedList ll = new FoldedLinkedList ();

        ll.insert (6);
        ll.insert (5);
        ll.insert (4);
        ll.insert (3);
        ll.insert (2);
        ll.insert (1);
        
        System.out.println("Linked List before fold");
        ll.display();

        ll.foldLinkedList (ll.head);
        
        System.out.println("Linked List after fold");
        ll.display ();
    }
}