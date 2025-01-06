// Give root of a binary tree, a target node and an integer k. Print the values of all the nodes that have a distance k from the target.
// time complexity = 0(n)
// space complexity = 0(ht of tree)

package DSA_Exercise.Trees;

public class AllNodesKDistanceAway {
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

    public static void Klevel(TreeNode node, int k, TreeNode blocker){
        if(node == null || node == blocker){
            return;
        }
        if(k == 0){
            System.out.println(node.val + " ");
        }
        Klevel(node.left, k-1, blocker);
        Klevel(node.right, k-1, blocker);
    }

    public static void KDistanceAway(TreeNode root, int target, int k){
        fun(root, target, k);
    }

    public static int fun(TreeNode root, int target, int k){
        if(root == null){
            return -1;
        }
        if(root.val == target){
            Klevel(root, k, null);
            return 1;
        }
        int lans = fun(root.left, target,k);
        if(lans != -1){
            Klevel(root, k-lans, root.left);
            return lans + 1;
        }

        int rans = fun(root.right, target,k);
        if(rans != -1){
            Klevel(root, k-lans, root.right);
            return rans + 1;
        }
        return -1;
    }
}
