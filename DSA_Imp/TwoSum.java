// Give an array of size N and an integer 'target'.Find the indices(i, j) of two numbers such that their sum is equal to target. (i!=j) You can assume that there will be exactly one solution
// Sample input 
// N=5
// arr={7,6,3,8,2}
// target = 14
// Sample Output = 1 3
// Time complexity = O(n^2)
// Space complexity = O(1)

package DSA_Imp;
import java.util.*;

public class TwoSum {
    public static void main(String[] args){
        int[] arr = {11, 3, 7, 9, 14, 2};
        int target = 17;
        int[] ans = new int[2];

        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i<arr.length; i++){
            int sno = target - arr[i];
            if(map.containsKey(sno)){
                ans[0] = map.get(sno);
                ans[1]=i;
                break;
            }
            map.put(arr[i], i);
        }
        System.out.println(ans[0] + " " + ans[1]);
    }
}
