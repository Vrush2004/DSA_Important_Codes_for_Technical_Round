// Give root of a binary tree, a target node and an integer k. Print the values of all the nodes that have a distance k from the target.


package DSA_Imp.Trees;

public class AllNodesKDistanceAway {
    public static void main(String[] args){

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

    public static void KDistanceAway(TreeNode root, int target, int k){
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
}
