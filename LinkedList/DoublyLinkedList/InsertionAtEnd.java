package LinkedList.DoublyLinkedList;

public class InsertionAtEnd {
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



  public void insertEnd (int data)
  {
    // Creating newNode memory & assigning data value
    Node freshNode = new Node (data);

    // assign data
    // since this will be the last node its next will be NULL
    freshNode.next = null;

    //if we are entering the first node
    if (head == null)
      {
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
    InsertionAtEnd doublylist = new InsertionAtEnd ();

      doublylist.insertEnd (3);
      doublylist.insertEnd (2);
      doublylist.insertEnd (1);
      doublylist.insertEnd (4);
      doublylist.insertEnd (5);

      doublylist.printList ();

  }
}