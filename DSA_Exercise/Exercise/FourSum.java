// Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
// Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
// The solution set must not contain duplicate quadruplets.
// Example: Given array S = {1 0 -1 0 -2 2}, and target = 0 A solution set is:
// (-2, -1, 1, 2)
// (-2,  0, 0, 2)
// (-1,  0, 0, 1)

package DSA_Exercise.Exercise;
import java.util.*;

public class FourSum {

    // Method to find all unique quadruplets
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);  // Sort the array to make it easier to avoid duplicates
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;  // Skip duplicates for 'a'
            
            for (int j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;  // Skip duplicates for 'b'
                
                int left = j + 1, right = nums.length - 1;
                
                while (left < right) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    
                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left++;
                        right--;
                        
                        // Skip duplicates for 'c' and 'd'
                        while (left < right && nums[left] == nums[left - 1]) left++;
                        while (left < right && nums[right] == nums[right + 1]) right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        // Assuming you are getting ArrayList<Integer> as input, convert it to int[] array
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1, 0, -1, 0, -2, 2)); // Example input
        int target = 0;

        // Convert ArrayList to int[] (primitive array)
        int[] nums = A.stream().mapToInt(Integer::intValue).toArray();

        // Call the fourSum method
        List<List<Integer>> result = fourSum(nums, target);
        
        // Printing the result
        for (List<Integer> quadruplet : result) {
            System.out.println(quadruplet);
        }
    }
}