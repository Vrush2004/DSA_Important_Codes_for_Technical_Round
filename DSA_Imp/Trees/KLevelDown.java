// Give a binary tree and a target node. Print all the nodes k level down from the target node.
// time complexity = 0(n)
// space complexity = 0(ht of tree)

package DSA_Imp.Trees;

public class KLevelDown{
    public static void main(String[] args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        int target = 2;  
        int k = 1;      
        System.out.println("Nodes " + k + " level(s) down from target " + target + ":");
        fun(root, target, k);
    }

    public static void fun(TreeNode root, int target, int k){
        if(root == null){
            return;
        }
        if(root.val == target){
            Klevel(root, k);
            return;
        }
        fun(root.left, target,k);
        fun(root.right, target,k);
    }

    public static void Klevel(TreeNode node, int k){
        if(node == null){
            return;
        }
        if(k == 0){
            System.out.println(node.val + " ");
        }
        Klevel(node.left, k-1);
        Klevel(node.right, k-1);
    }
}