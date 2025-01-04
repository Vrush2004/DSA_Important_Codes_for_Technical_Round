package LinkedList.SinglyLinkedList;

public class DeleteAlternateNode {
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
    public DeleteAlternateNode ()
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
              System.out.print (temp.data + "-->");
              // Set temp to point to the next node
              temp = temp.next;
          }
          System.out.println ("END");
    }
}