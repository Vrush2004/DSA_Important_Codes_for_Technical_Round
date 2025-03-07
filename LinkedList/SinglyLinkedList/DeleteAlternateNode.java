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

    public void deleteAlternateNodes ()
    {
      this.deleteAlternateNodes (this.head);
    }

    //Function to delete alternate nodes in linked list
    private void deleteAlternateNodes (Node node)
    {
        //Base case
        if (node == null)
        {
            return;
        }
        Node nm1 = this.head;
        Node n = nm1.next;
        while (nm1 != null && n != null)
        {
            nm1.next = n.next;
            nm1 = n.next;
            if (nm1 != null)
            {
                n = nm1.next;
            }
        }
    }

    public static void main (String[]args) throws Exception
    {
      DeleteAlternateNode ll = new DeleteAlternateNode ();
        ll.addFirst (70);
        ll.addFirst (60);
        ll.addFirst (50);
        ll.addFirst (40);
        ll.addFirst (30);
        ll.addFirst (20);
        ll.addFirst (10);
        ll.display ();
        ll.deleteAlternateNodes ();
        ll.display ();
    }
}