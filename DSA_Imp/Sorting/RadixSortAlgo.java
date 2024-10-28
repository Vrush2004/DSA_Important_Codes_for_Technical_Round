// Sort the given array using radix sort algorithm.
// time complexity = O(d*(N+R))
// space complexity = 0(N)

package DSA_Imp.Sorting;

public class RadixSortAlgo {
    public static void main(String[] args){
        int [] arr = {879, 645, 80, 345, 108, 254, 789, 657};
        radixSort(arr);
        for(int val : arr){
            System.out.print(val + " ");
        }
    }

    public static void radixSort(int[] arr){
        int max = arr[0];
        for(int i=1; i< arr.length; i++){
            max = Math.max(max, arr[i]);
        }

        int exp = 1;
        while (max > 0) {
            max /= 10;
            countSort(arr, exp);
            exp *= 10;
        }
    }

    public static void countSort(int[] arr, int exp){
        int n = arr.length;
        int[] p = new int[10];

        // 1. Create the frequency array
        for (int i=0; i<n; i++){
            p[(arr[i] / exp) % 10]++;
        }

        // 2. Convert the p array into prefix sum array
        for(int i=1; i<p.length; i++){
            p[i] += p[i-1];
        }

        // 3. Traverse on the original array and update ans[]
        int[] ans = new int[n];
        for(int i=n-1; i>=0; i--){
            int digit = (arr[i] / exp) % 10;
            int pos = p[digit] - 1;
            ans[pos] = arr[i];
            p[digit]--;
        }

        // Copy ans into the original array
        for(int i=0; i<ans.length; i++){
            arr[i] = ans[i];
        }
    }
}
