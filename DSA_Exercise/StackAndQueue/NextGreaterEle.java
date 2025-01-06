// Given an array of size N.Find the next greater number for every element in the array.
// The next greater number of x is first greater number present to its right. If it doesn't exist, return -1 for that number.
// Sample input 
// arr = {7, 6, 3, 8, 2, 11, 30, 5, 25}
// sample output
// {8, 8, 8, 11, 11, 30, -1, 25, -1}
// time complexity = 0(n)
// space complexity = 0(n) 

package DSA_Exercise.StackAndQueue;
import java.util.*;

public class NextGreaterEle {
    public static void main(String[] args){
        int[] arr = {5,9,21, 11, 17, 3, 30, 12, 25, 50};
        int[] ans = greaterEle(arr);
        for(int a : ans){
            System.out.print(a + " ");
        }
        System.out.println();
    }

    public static int[] greaterEle2(int[] arr){
        Stack<Integer> st = new Stack<>();
        int[] ans = new int[arr.length];
        st.push(0);

        for(int i = 1; i<arr.length; i++){
            // Pop all smaller elements
            // for all these smaller elements, nge is current element
            while(st.size() > 0 && arr[st.peek()] < arr[i]){
                ans[st.peek()] = arr[i];
                st.pop();
            }
            st.push(i);
        }
        while (st.size() > 0) {
            ans[st.pop()] = -1;
        }
        return ans;
    }

    public static int[] greaterEle(int[] arr){
        Stack<Integer> st = new Stack<>();
        int[] ans = new int[arr.length];
        for(int i = arr.length-1; i>=0; i--){
            // pop all smaller elements
            while(st.size() > 0 && st.peek() < arr[i]) {
                st.pop();
            }

            // update ans
            if(st.size() == 0){
                ans[i] = -1;
            }
            else{
                ans[i] = st.peek();
            }

            // add current element in the stack
            st.push(arr[i]);
        }
        return ans;
    }
}