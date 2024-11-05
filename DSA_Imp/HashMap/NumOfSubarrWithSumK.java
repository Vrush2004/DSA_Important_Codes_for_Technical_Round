// Given an unsorted array of integers and an integer K. You need to find the number of subarrays with sum = K.
// Sample input 
// arr = {9, 4, 20, 3, 10, 5}, k = 33
// Sample output = 2
// Time complexity = O(n)
// Space complexity = O(n)

package DSA_Imp.HashMap;

import java.util.HashMap;

public class NumOfSubarrWithSumK {
    public static void main(String[] args){
        int[] arr = {9, 4, 20, 3, 10, 5};
        System.out.println(subArrWithSumK(arr, 33));
    }

    public static int subArrWithSumK(int[] arr, int target){
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int ans = 0;

        int psum = 0;
        for(int i = 0; i< arr.length; i++){
            psum += arr[i];
            if(map.containsKey(psum - target) == true){
                ans += map.get(psum - target);
            }
            map.put(psum, map.getOrDefault(psum, 0) + 1);
        }
        return ans;
    }
}