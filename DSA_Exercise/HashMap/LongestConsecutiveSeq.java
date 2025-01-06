// Given an unsorted array of integers. You need to find the length of the longest consecutive elements sequence.
// Sample input 
// arr ={0,3,7,2,5,8,4,6,0,1}
// Sample output = 9
// Time complexity = O(n)
// Space complexity = O(n)

package DSA_Exercise.HashMap;
import java.util.*;

public class LongestConsecutiveSeq {
    public static void main(String[] args){
        int[] arr = {11, 7, 1, 17, 6, 2, 3, 16, 8, 4, 9, 10, 15};
        System.out.println(longestConSeq(arr));
    }

    public static int longestConSeq(int[] arr){
        HashMap<Integer, Boolean> map = new HashMap<>();
        // 1. Assume every element as the sp of lcs
        for(int i = 0; i<arr.length; i++){
            map.put(arr[i], true);
        }

        // 2. Consider only valid sp
        for(int i = 0; i<arr.length; i++){
            if(map.containsKey(arr[i] - 1) == true){
                map.put(arr[i], false);
            }
        }

        // 3. For every valid starting point, find length of lcs
        int maxlen = 1;
        for(int i = 0; i<arr.length; i++){
            if(map.get(arr[i]) == true){
                int currlen = 1;
                int val = arr[i];
                while (map.containsKey(val+1) == true) {
                    currlen++;
                    val++;
                }
                maxlen = Math.max(maxlen, currlen);
            }
        }
        return maxlen;
    }
}