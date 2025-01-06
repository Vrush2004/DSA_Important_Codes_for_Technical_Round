// Given an integer array of size N and an integer target. Print all the subsets for which the sum is equal to the target.
// Sample input
// arr = {10, 20, 30, 40, 50}
// target=60
// Sample output
// 10 20 30
// 10, 50
// 20, 40
// time complexity = 0(2^n)
// space complexity = 0(n)

package DSA_Exercise.RecursionAndBacktracking;

import java.util.ArrayList;

public class TargetSumSubset {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};  
        int target = 60;                  
        
        System.out.println("Subsets whose sum equals " + target + ":");
        tss(arr, 0, target, new ArrayList<>());
    }

    public static void tss(int[] arr, int i, int target, ArrayList<Integer> ans) {
        if (i == arr.length) {  
            if (target == 0) {  
                System.out.println(ans);
            }
            return;
        }

        ans.add(arr[i]);
        tss(arr, i + 1, target - arr[i], ans); 
        ans.remove(ans.size() - 1);  

        tss(arr, i + 1, target, ans); 
    }
}