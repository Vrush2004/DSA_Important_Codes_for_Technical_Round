// Given an array of size N which contains all thenumbers from 0 to N-1. Find the minimum number of swaps required to the sort the array.
// Sample input
// arr = {0,4,3,2,1}
// Sample output
// 2
// time complexity = O(n)
// space complexity = O(n)

package DSA_Exercise.Graphs;

public class MinswapsToSortArr {
    public static void main(String[] args){
        int[] arr = {2,4,5,1,3,6,0};
        System.out.println(minSwaps(arr));
    }

    public static int minSwaps(int[] arr){
        int ans = 0;
        boolean[] visited = new boolean[arr.length];

        for(int i = 0; i<arr.length; i++){
            if(!visited[i]){
                visited[i] = true;
                int j = i;
                int len = 1;

                while (arr[j] != i) {
                    j = arr[j];
                    visited[j] = true;
                    len++;
                }
                ans += (len - 1);
            }
        }
        return ans;
    }
}