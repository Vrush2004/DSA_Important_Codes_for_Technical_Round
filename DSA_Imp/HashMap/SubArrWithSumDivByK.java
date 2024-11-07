// Given an array of size N and an integer 'K'. Find the count of subarrays with the sum of elements divisible by K.
// Sample input 
// arr = {2, 7, 6, 1, 4, 5}, k=3
// Sample output = 5
// Time complexity = O(n)
// Space complexity = O(n)

package DSA_Imp.HashMap;

import java.util.HashMap;

public class SubArrWithSumDivByK {
    public static void main(String[] args) {
        int[] arr = {2, 7, 6, 1, 4, 5};
        int k = 3;

        System.out.println(countSubarraysWithSumDivisibleByK(arr, k));
    }

    public static int countSubarraysWithSumDivisibleByK(int[] arr, int k) {
        // Create a hashmap to store the frequency of remainders
        HashMap<Integer, Integer> remainderFreq = new HashMap<>();
        
        // Initialize hashmap with remainder 0 having frequency 1 (for subarrays starting from index 0)
        remainderFreq.put(0, 1);
        
        int prefixSum = 0;
        int count = 0;

        // Traverse through the array
        for (int num : arr) {
            // Update prefix sum
            prefixSum += num;

            // Calculate remainder when prefix sum is divided by k
            int remainder = prefixSum % k;

            // Handle negative remainders (in case prefixSum is negative)
            if (remainder < 0) {
                remainder += k;
            }

            // If remainder has been seen before, it means there are subarrays that are divisible by k
            if (remainderFreq.containsKey(remainder)) {
                count += remainderFreq.get(remainder);
            }

            // Update the frequency of the current remainder
            remainderFreq.put(remainder, remainderFreq.getOrDefault(remainder, 0) + 1);
        }

        return count;
    }
}
