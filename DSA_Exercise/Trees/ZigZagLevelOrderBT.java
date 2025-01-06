// time complexity = 0(n)
// space complexity = 0(n)

package DSA_Exercise.Trees;
import java.util.*;

public class ZigZagLevelOrderBT {
    public static void main(String[] args){
        Integer[] arr = {2,7,2,null, null,6,5,null, null, 11, null, null, 5, null, 9, 4, null, null, null};
        TreeNode root = construct(arr);
        printLevelOrderZigZag(root);
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

    public static void printLevelOrderZigZag(TreeNode root){
        Stack<TreeNode> curr = new Stack<>();
        Stack<TreeNode> next = new Stack<>();

        curr.push(root);
        int level = 0;

        while(curr.size() != 0){
            while(curr.size() != 0){
                TreeNode rn = curr.pop();
                System.out.print(rn.val + " ");
                if(level % 2 == 0){
                    if(rn.left != null) {next.push(rn.left);}
                    if(rn.right != null) {next.push(rn.right);}
                }else{
                    if(rn.right != null) {next.push(rn.right);}
                    if(rn.left != null) {next.push(rn.left);}
                }
            }
            System.out.println();
            level++;
            
            curr = next;
            next = new Stack<>();
        }
    }
}