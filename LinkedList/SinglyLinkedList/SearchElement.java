package LinkedList.SinglyLinkedList;

public class SearchElement {
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
    //searchNode() will search for a given node in the list
    public void searchNode (int data)
    {
        Node current = head;
        int i = 1;
        boolean flag = false;

        //Checks whether list is empty
        if (head == null)
          {
              System.out.println ("List is empty");
          }
        else
          {
              while (current != null)
              {
                //Compares node to be found with each node present in the list
                if (current.data == data)
                  {
              flag = true;
              break;
                  }
                i++;
                current = current.next;
              }
          }
          if (flag)
              System.out.println ("Element is present in the list at the position : " + i);
          else
              System.out.println ("Element is not present in the list");
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
        SearchElement ll = new SearchElement ();

          ll.insert (6);
          ll.insert (5);
          ll.insert (4);
          ll.insert (3);
          ll.insert (2);
          ll.insert (1);

        //Search for node 2 in the list
          ll.searchNode (2);
        //Search for a node  in the list
          ll.searchNode (7);
    }
}