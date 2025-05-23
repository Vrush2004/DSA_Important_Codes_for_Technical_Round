// Given an array of intervals in any order, merge all overlapping intervals into one and return an array of non-overlapping intervals.
// Sample input
// intervals = {{1,4},{2,5},{7,14},{6,11}}
// sample output
// {{1,5}, {6,14}}
// time complexity = 0(nlogn)
// space complexity = 0(n) 

package DSA_Exercise.StackAndQueue;
import java.util.*;

public class MergeIntervals {
    public static void main(String[] args){
        int[][] intervals = {{1,4}, {8,12}, {3,7}, {2,6},{9,11}, {17,25}, {15,21}};
        int[][] ans = mergeInterval(intervals);
        for(int[] arr : ans){
            System.out.println(arr[0] + " " + arr[1]);
        }
    }

    public static int[][] mergeInterval(int[][] intervals){
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        Stack<int[]> st = new Stack<>();
        st.push(intervals[0]);
        for(int i=1; i< intervals.length; i++){
            if(st.peek()[1] >= intervals[i][0]){
                st.peek()[1] = Math.max(st.peek()[1], intervals[i][1]);
            }else{
                st.push(intervals[i]);
            }
        }
        int[][] ans = new int[st.size()][2];
        for(int i= ans.length -1; i >= 0; i--){
            ans[i][0] = st.peek()[0];
            ans[i][1] = st.peek()[1];
            st.pop();
        }
        return ans;
    }
}
