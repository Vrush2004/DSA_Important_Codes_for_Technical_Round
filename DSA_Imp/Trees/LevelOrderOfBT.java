// time complexity = 0(n)
// space complexity = 0(n)

package DSA_Imp.Trees;
import java.util.*;

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

public class LevelOrderOfBT {
    public static void main(String[] args){
        Integer[] arr = {2,7,2,null, null,6,5,null, null, 11, null, null, 5, null, 9, 4, null, null, null};
        TreeNode root = construct(arr);
        printLevelOrder(root);
    }

    public static TreeNode construct(Integer[] arr){
        if (arr.length == 0 || arr[0] == null) return null;

        TreeNode root = new TreeNode(arr[0]);
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);

        int i = 1;
        while (!queue.isEmpty() && i < arr.length) {
            TreeNode current = queue.poll();

            if (arr[i] != null) {
                current.left = new TreeNode(arr[i]);
                queue.add(current.left);
            }
            i++;

            if (i < arr.length && arr[i] != null) {
                current.right = new TreeNode(arr[i]);
                queue.add(current.right);
            }
            i++;
        }
        return root;
    }

    public static void printLevelOrder(TreeNode root){
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);

        while(q.size() > 0){
            int removals = q.size();
            for(int i = 0; i<removals; i++){
                TreeNode rn = q.remove();
                System.out.print(rn.val + " ");
                if(rn.left != null) {q.add(rn.left);}
                if(rn.right != null) {q.add(rn.right);}
            }
            System.out.println();
        }
    }
}