// Sort the given array of strings representing dates in DDMMYYYY format.
// time complexity = O(N+R)
// space complexity = O(N+R)

package DSA_Exercise.Sorting;

public class sortDates {
    public static void main(String[] args){
        String[] arr = {"05121968", "17121996", "05061997", "11081972", "11081990"};
        sort(arr);
        for (String s : arr){
            System.out.print(s + " ");
        }
    }

    public static void sort(String[] arr){
        // Sort by day (DD)
        countSort(arr, 31, 1000000, 100);

        // Sort by month (MM)
        countSort(arr, 12, 10000, 100);

        // Sort by year (YYYY)
        countSort(arr, 2500, 1, 10000);
    }

    public static void countSort(String[] arr, int range, int div, int mod){
        int n = arr.length;
        int[] p = new int[range + 1];

        // 1. Create the frequency array
        for (int i = 0; i < n; i++) {
            int key = (Integer.parseInt(arr[i]) / div) % mod;
            p[key]++;
        }

        // 2. Convert the p array into prefix sum array
        for (int i = 1; i < p.length; i++) {
            p[i] += p[i - 1];
        }

        // 3. Traverse the original array and update ans[]
        String[] ans = new String[n];
        for (int i = n - 1; i >= 0; i--) {
            int key = (Integer.parseInt(arr[i]) / div) % mod;
            int pos = p[key] - 1;
            ans[pos] = arr[i];
            p[key]--;
        }

        // Copy ans into the original array
        for (int i = 0; i < n; i++) {
            arr[i] = ans[i];
        }
    }
}
