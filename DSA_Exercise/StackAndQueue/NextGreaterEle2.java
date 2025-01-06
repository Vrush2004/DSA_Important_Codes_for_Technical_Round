// Given a circular array. Find the next greater number for every element in the circular array.
// The next greater number of x is first greater number present to its right. If it doesn't exist, return -1 for that number.
// sample input
// arr = {1,6,3,8,2}
// sample output
// ans = {6,8,8,-1,6}
// time complexity = 0(n)
// space complexity = 0(n) 

package DSA_Exercise.StackAndQueue;

import java.util.*;

public class NextGreaterEle2 {
    public static void main(String[] args){
        int[] arr = {5,9,21, 11, 17, 3, 30, 12, 25, 50};
        int[] ans = greaterEle(arr);
        for(int a : ans){
            System.out.print(a + " ");
        }
        System.out.println();
    }

    public static int[] greaterEle(int[] arr){
        int n = arr.length;
        Stack<Integer> st = new Stack<>();
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        st.push(0);

        for(int i = 1; i<2*arr.length; i++){
            while (st.size() > 0 && arr[st.peek()] < arr[i]) {
                ans[st.pop()] = arr[i % n];
            }
            st.push(i % n);
        }
        return ans;
    }
}