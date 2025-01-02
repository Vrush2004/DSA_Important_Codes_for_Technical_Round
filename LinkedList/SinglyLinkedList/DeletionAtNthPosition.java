package LinkedList.SinglyLinkedList;

public class DeletionAtNthPosition {
    Node head;

    // Node Class
    class Node{
        int data;
        Node next;

        Node(int val)
        {
            data = val;
            next = null;
        }

    }

    public void deleteNthNode(int n)
    {
        int len = calcLen(head);

        // Can only insert after 1st position
        // Can't insert if position to insert is greater than size of Linked List
        if(n < 1 || n > len)
        {
            System.out.println("Can't delete\n");

        }
        else
        {
            if(n == 1)
            {
                // head has to be deleted
                System.out.println("Deleted: " + head.data);
                head = head.next;
                return;
            }
            // required to traverse
            Node temp = head;
            Node previous = null;

            // traverse to the nth node
            while(--n > 0) {
                previous = temp;
                temp = temp.next;
            }
            // assigned next node of the previous node to nth node's next
            previous.next = temp.next;
            System.out.println("Deleted: " + temp.data);
        }
    }
    public void insert(int data)
    {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    public void showList()
    {
        Node temp = head;
        //as linked list will end when Node reaches Null
        while(temp!=null)
        {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println("\n");
    }

    public int calcLen(Node temp){
        int len = 0;

        while(temp!=null){
            temp = temp.next;
            len++;
        }
        return len;
    }
    public static void main(String args[])
    {
        DeletionAtNthPosition ll = new DeletionAtNthPosition();

        ll.insert(35);
        ll.insert(34);
        ll.insert(33);
        ll.insert(32);
        ll.insert(31);
        ll.insert(30);

        ll.showList();

        ll.deleteNthNode(3);
        ll.deleteNthNode(4);
        ll.showList();
    }
}