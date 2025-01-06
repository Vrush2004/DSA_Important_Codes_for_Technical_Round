// Give an array and a "target". You need to find all the triplets (a[i], a[j], a[k]) such that a[i]+ a[j]+ a[k] = target and i!=j!=k.
// Sample input 
// N=7
// arr = {7, -6, 3, 8, -1, 8, -1}
// target=0
// sample output = [-11,3,8],[-6,-1,7]
// Time complexity = O(n^2) 
// Space complexity = O(1)

package DSA_Exercise.Arrays;
import java.util.*;

public class ThreeSum{
    public static void main(String[] args){
        int[] arr = {7, -6, 3, 8, -1, 8, -11};
        int target = 0;
        solution(arr, target, arr.length);
    }
    public static void solution(int[] a, int target, int n){
        Arrays.sort(a);
        for(int i=0; i<n; i++){
            if(i==0 || a[i] != a[i-1]){
                int j=i+1, k=n-1;
                int tar = target-a[i];
                while (j<k){
                    if(a[j] + a[k] == tar){
                        System.out.println(a[i] + " " + a[j] + " " + a[k]);
                        while (j<k && a[j] == a[j+1]) j++;
                        while (j<k && a[k] == a[k-1]) k--;
                        j++;
                        k--;
                    }else if (a[j] + a[k] < tar){
                        j++;
                    }
                    else{
                        k--;
                    }
                }
            }
        }
    }
}