// Give root of a binary tree. You need to find the minimum number of cameras to monitor all nodes of the tree.
// Note -> If you install camera at a particular node, it can monitor its parent, itself and its immediate children.
// time complexity = 0(n)
// space complexity = 0(n)

package DSA_Exercise.Trees;

public class CamerasInBT {
    public static void main(String[] args) {
        Integer[] arr = {2, 3, 5, null, null, 6, 7, null, 8, 9, null, null, 10, null, null, null, 11, 12, null};
        TreeNode root = construct(arr);
        int ansForRoot = minCameras(root);
        if (ansForRoot == -1) {
            cameras++;
        }
        System.out.println("Minimum number of cameras required: " + cameras);
    }

    static int cameras = 0;

    public static int minCameras(TreeNode root) {
        if (root == null) {
            return 0; // Covered by a camera
        }

        int leftStatus = minCameras(root.left);
        int rightStatus = minCameras(root.right);

        // If either left or right child is not covered, place a camera here
        if (leftStatus == -1 || rightStatus == -1) {
            cameras++;
            return 1; // Camera placed here
        }

        // If either left or right child has a camera, this node is covered
        if (leftStatus == 1 || rightStatus == 1) {
            return 0; // This node is covered without a camera
        }

        // If both children are covered but do not have cameras, this node is not covered
        return -1;
    }

    // Method to construct a binary tree from the given array
    public static TreeNode construct(Integer[] arr) {
        if (arr == null || arr.length == 0) return null;
        return constructTree(arr, new int[]{0});
    }

    private static TreeNode constructTree(Integer[] arr, int[] index) {
        if (index[0] >= arr.length || arr[index[0]] == null) {
            index[0]++;
            return null;
        }
        TreeNode node = new TreeNode(arr[index[0]++]);
        node.left = constructTree(arr, index);
        node.right = constructTree(arr, index);
        return node;
    }
}