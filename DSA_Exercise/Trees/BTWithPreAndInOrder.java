// Give two integers arrays of unique values. pre[] represents preorder traversal of a binary tree. in[] represents inorder traversal of a binary tree.
// Sample input
// pre[] = {5,7,15,20,9}
// in[] = {7,5,20,15,9}
// time complexity = 0(n^2)
// space complexity = 0(n)

package DSA_Exercise.Trees;

class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(){

    }
    TreeNode(int val){
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class BTWithPreAndInOrder {
    public static void main(String[] args){
        int[] pre = {5, 7, 15, 20, 9};
        int[] in = {7, 5, 20, 15, 9};
        TreeNode root = constructTree(pre, 0, pre.length - 1, in, 0, in.length - 1);

        printInOrder(root);
    }

    public static TreeNode constructTree(int[] pre, int si1, int ei1, int[] in, int si2, int ei2){
        if(si1 > ei1){
            return null;
        }

        if(si1 == ei1){
            return new TreeNode(pre[si1]);
        }

        TreeNode root = new TreeNode(pre[si1]);
        int idx = -1;
        for(int i = si2 ; i <= ei2; i++){
            if(in[i] == pre[si1]){
                idx = i;
                break;
            }
        }

        root.left = constructTree(pre, si1+1, si1 + idx - si2, in, si2, idx-1);
        root.right = constructTree(pre, si1 + idx - si2 + 1, ei1, in, idx+1, ei2);
        return root;
    }

    public static void printInOrder(TreeNode root) {
        if (root == null) return;
        printInOrder(root.left);
        System.out.print(root.val + " ");
        printInOrder(root.right);
    }
}
