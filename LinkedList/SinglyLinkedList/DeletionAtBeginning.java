package LinkedList.SinglyLinkedList;

public class DeletionAtBeginning {
        Node head;
    
        // Node Class
        class Node{
            int data;
            Node next;
    
            Node(int x) // parameterized constructor
            {
                data = x;
                next = null;
            }
        }
        public void deleteStart()
        {
            if (head == null){
                System.out.println("List is empty, not possible to delete");
                return;
            }
    
            System.out.println("Deleted: " + head.data);
            // move head to next node
            head = head.next;
        }
    
        public Node insert(int data)
        {
            Node newNode = new Node(data);
            newNode.next = head;
            head = newNode;
    
            return head;
        }
    
        public void display()
        {
            Node node = head;
            //as linked list will end when Node reaches Null
            while(node!=null)
            {
                System.out.print(node.data + " ");
                node = node.next;
            }
            System.out.println("\n");
        }
        public static void main(String args[])
        {
            DeletionAtBeginning ll = new DeletionAtBeginning();
    
            ll.insert(6);
            ll.insert(5);
            ll.insert(4);
            ll.insert(3);
            ll.insert(2);
            ll.insert(1);
    
            ll.display();
    
            ll.deleteStart();
            ll.display();
    
            ll.deleteStart();
            ll.deleteStart();
            ll.deleteStart();
            ll.display();
        }   
}