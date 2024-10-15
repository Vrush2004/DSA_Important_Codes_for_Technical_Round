// Given an array of size N which contains distinct integers. You have to print all the possible permutations
// Sample input
// arr = {1,2,3}
// Sample output
// 1 2 3
// 1 3 2
// 2 1 3
// 2 3 1
// 3 1 2
// 3 2 1
// time complexity = 0(n!*n)
// space complexity = 0(n)

package DSA_Imp.RecursionAndBacktracking;

import java.util.*;

public class PrintPermutation {
    public static void main(String[] args){
        int[] arr = {1,2,3};
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
}
