// Give an array. You need to find the majority element in the array.
// Majority element is defined as the element which is appearing more than n/2 times in the array of length n.
// Sample input 
// N=10
// arr ={2,2,6,6,6,2,2,8,2,2}
// Sample output = 2
// time complexity = 0(n)
// space complexity = 0(n)

package DSA_Imp.Arrays;

public class MajorityEle {
    public static void main(String[] args){
        int[] arr = {5, 7, 4, 7, 4, 4, 5, 4, 4, 7, 4, 4};
        System.out.println(findMajorityElement(arr, arr.length));
    }

    public static int findMajorityElement(int[] arr, int n){
        int candidate = arr[0];
        int count = 1;

        for (int i=1; i<n;i++){
            if(arr[i] == candidate){
                count++;
            }else{
                count--;
            }

            if(count == 0){
                candidate= arr[i];
                count=1;
            }
        }

        count=0;
        for (int val: arr){
            if(val == candidate){
                count++;
            }
        }
        if(count > n/2){
            return candidate;
        }else{
            return -1;
        }
    }
}
