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

package DSA_Imp.RecursionAndBacktracking;

import java.util.ArrayList;

public class TargetSumSubset {
    public static void main(String[] args){
        int[] arr = {10, 20, 30, 40, 50};
        permutations(arr, 0, new boolean[arr.length] , new ArrayList<>());
    }

    public static void permutations(int[] arr, int pos, boolean[] selected, ArrayList<Integer> ans){
        if(pos == arr.length){
            System.out.println(ans);
            return;
        }

        for(int i = 0; i < arr.length; i++){
            if(selected[i] == false){
                selected[i] = true;
                ans.add(arr[i]);
                permutations(arr, pos + 1, selected, ans);
                selected[i] = false;
                ans.remove(ans.size() - 1);
            }
        }
    }

    public static void tss(int[] arr, int i, int target, ArrayList<Integer> ans){
        if(target < 0){
            return;
        }

        if(i == arr.length){
            if(target == 0)
            System.out.println(ans);
            return;
        }

        // select ith element
        ans.add(arr[i]);
        tss(arr, i+1, target - arr[i], ans);
        ans.remove(ans.size() - 1);

        // reject ith element
        tss(arr, i+1, target, ans);
    }
}
