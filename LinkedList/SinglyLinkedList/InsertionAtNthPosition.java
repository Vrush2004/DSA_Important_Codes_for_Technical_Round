package LinkedList.SinglyLinkedList;

public class InsertionAtNthPosition {
        Node head;
    
        // Node Class
        class Node{
            int data;
            Node next;
    
            Node(int x)
            {
                data = x;
                next = null;
            }
        }
        public Node insertBeginning(int data)
        {
            Node newNode = new Node(data);
            newNode.next = head;
            head = newNode;
    
            return head;
        }
    
        public void insertAfter(int n,int data)
        {
            int size = calcSize(head);
    
            // Can only insert after 1st position
            // Can't insert if position to insert is greater than size of Linked List
            if(n < 1 || n > size)
            {
                System.out.println("Can't insert\n");
    
            }
            else
            {
                Node newNode = new Node(data);
                // required to traverse
                Node temp = head;
    
                // traverse to the nth node
                while(--n > 0)
                    temp=temp.next;
    
                newNode.next= temp.next;
                temp.next = newNode;
            }
        }
}