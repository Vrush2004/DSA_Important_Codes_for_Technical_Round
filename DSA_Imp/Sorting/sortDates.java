// Sort the given array of strings representing dates in DDMMYYYY format.

package DSA_Imp.Sorting;

public class sortDates {
    public static void main(String[] args){
        String[] arr = {"05121968", "17121996", "05061997","11081972", "11081990"};
        sort(arr);
        for (String s : arr){
            System.out.print(s + " ");
        }
    }

    public static void sort(String[] arr){

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