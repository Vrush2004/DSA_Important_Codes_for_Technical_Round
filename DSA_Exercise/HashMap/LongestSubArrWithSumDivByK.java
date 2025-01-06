// Given an array of size N and an integer K. Find the longest subarray's length with the sum of elements divisible by K.
// Sample input 
// arr ={2, 7, 6, 1, 4, 5}, k=3
// Sample output = 4
// Time complexity = O(n)
// Space complexity = O(n)

package DSA_Exercise.HashMap;
import java.util.*;

public class LongestSubArrWithSumDivByK {
    public static void main(String[] args){
        int[] arr = {2, 4, 8, 1, 3, 6, 2, 9, 3, 11};
        System.out.println(longSubarray(arr,5));
    }

    public static int longSubarray(int[] arr, int k){
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int sum = 0;
        int maxlen = 0;

        for(int i=0; i<arr.length; i++){
            sum += arr[i];
            int mod = ((sum % k) + k) % k;

            if(map.containsKey(mod) == true){
                maxlen = Math.max(maxlen, i-map.get(mod));
            }else{
                map.put(mod, i);
            }
        }
        return maxlen;
    }
}