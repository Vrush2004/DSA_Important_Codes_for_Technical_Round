// Sort the given array using merge sort algorithm.
// sample input
// arr = {5,7,-2,11,6,4,9,1}
// sample output 
// ans = {-2,1,4,5,6,7,9,11}
// time complexity = O(nlogn)
// space complexity = O(n)

package DSA_Imp.Sorting;

public class MergeSort {
    public static void main(String[] args){
        int[] arr1 = {2,3,8,10,12,15};
        int[] arr2 = {3,5,7,11};
        int[] ans = mergeTwoArray(arr1, arr2);
        for (int val : ans){
            System.out.print(val + " ");
        }
    }

    public static int[] sort(int[] arr, int lo, int hi){
        if(lo == hi){
            int[] bans = new int[1];
            bans[0] = arr[lo];
            return bans;
        }

        int mid = (lo + hi) /2;
        int[] fsh = sort(arr, lo, mid);
        int[] ssh = sort(arr, mid + 1, hi);
        int[] ans = mergeTwoArray(fsh, ssh);
        return ans;
    }

    public static int[] mergeTwoArray(int[] arr1, int[] arr2){
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