// Sort the array using counting sort algorithm

package DSA_Exercise.Sorting;

public class CountingSortAlgo {
    public static void main(String[] args){
        int [] arr = {6,8,1,3,1,4,9,1,2,8,8,7};
        int[] ans = countSort(arr);
        for(int val : ans){
            System.out.print(val + " ");
        }
    }

    public static int[] countSort(int[] arr){
        int n = arr.length;
        int max = arr[0];
        for(int i=1; i< arr.length; i++){
            max = Math.max(max, arr[i]);
        }
        int[] p = new int[max+1];

        // 1.create the frequency array
        for (int i=0; i<n; i++){
            p[arr[i]]++;
        }
        // 2.convert the arr into prefixsum arr
        for(int i =1 ; i<p.length; i++){
            p[i] = p[i-1] + p[i];
        }
        // 3.traverse on the original array and try to update ans[]
        int[] ans = new int[n];
        for(int i=n-1; i>=0; i--){
            int pos = p[arr[i]];
            ans[pos-1] = arr[i];
            p[arr[i]]--;
        }

        return ans;
    }
}
