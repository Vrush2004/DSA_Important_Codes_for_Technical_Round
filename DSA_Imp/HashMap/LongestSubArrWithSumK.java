// Given an unsorted array of integers and an integer K. You need to find the largest subarray with sum = K.
// Sample input 
// arr ={10, 5, 2, 7, 1, 9}, k=15
// Sample output = 4
// Time complexity = O(n)
// Space complexity = O(n)

package DSA_Imp.HashMap;

import java.util.HashMap;

public class LongestSubArrWithSumK {
    public static void main(String[] args){
        int[] arr = {11, 7, 1, 17, 6, 2, 3, 16, 8, 4, 9, 10, 15};
        System.out.println(longestSubArray(arr, 33));
    }

    public static int longestSubArray(int[] arr, int target){
        int maxlen = -1;

        HashMap<Integer, Integer> map = new HashMap<>();
        // first occurence of the sum
        map.put(0, -1);  // to cover the edge case
    
        int psum = 0;
        for(int i=0; i<arr.length; i++){
            psum += arr[i];
            if(map.containsKey(psum - target) == true){
                maxlen = Math.max(maxlen, i - map.get(psum - target));
            }
            if(map.containsKey(psum) == false){
                // it this psum is appearing for the first time
                map.put(psum, i);
            }
        }
        return maxlen;
    }
}