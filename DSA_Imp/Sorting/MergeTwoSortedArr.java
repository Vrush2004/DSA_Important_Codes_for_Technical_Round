// Given two sorted arrays. Merge them to make a new sorted array.
// sample input 
// arr1 = {2,3,8,10,12,15}
// arr2 = {3,5,7,11}
// sample output 
// ans={2,3,3,5,7,8,10,11,12,15}
// time complexity = O(N+M)
// space complexity = O(1)

package DSA_Imp.Sorting;

public class MergeTwoSortedArr {
    public static void main(String[] args){
        int[] arr1 = {2,3,8,10,12,15};
        int[] arr2 = {3,5,7,11};
        int[] ans = mergeArray(arr1, arr2);
        for (int val : ans){
            System.out.print(val + " ");
        }
    }

    public static int[] mergeArray(int[] arr1, int[] arr2){
        int[] ans = new int[arr1.length + arr2.length];
        int i =0, j=0;
        int k =0;
        while(i < arr1.length && j < arr2.length){
            if(arr1[i] <= arr2[j]){
                ans[k] = arr1[i];
                i++;
                k++;
            }else{
                ans[k] = arr2[j];
                j++;
                k++;
            }
        }
        while (i < arr1.length) {
            ans[k] = arr1[i];
            i++;
            k++;
        }
        while(j < arr2.length){
            ans[k] = arr2[j];
            j++;
            k++;
        }
        return ans;
    }
}