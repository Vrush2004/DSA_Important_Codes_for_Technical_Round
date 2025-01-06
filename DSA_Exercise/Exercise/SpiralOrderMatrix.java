// Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.

package DSA_Exercise.Exercise;
import java.util.*;

public class SpiralOrderMatrix {
    public int[][] generateMatrix(int A) {
        int[][] matrix = new int[A][A];
        
        int top = 0, bottom = A - 1, left = 0, right = A - 1;
        int num = 1; // Start filling with 1
        
        // Loop until all elements are filled
        while (top <= bottom && left <= right) {
            // Fill the top row
            for (int i = left; i <= right; i++) {
                matrix[top][i] = num++;
            }
            top++; // Move the top boundary down
            
            // Fill the right column
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = num++;
            }
            right--; // Move the right boundary left
            
            // Fill the bottom row
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = num++;
                }
                bottom--; // Move the bottom boundary up
            }
            
            // Fill the left column
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    matrix[i][left] = num++;
                }
                left++; // Move the left boundary right
            }
        }
        
        return matrix;
    }

    public static void main(String[] args) {
        SpiralOrderMatrix obj = new SpiralOrderMatrix();
        
        // Test case 1: A = 1
        int[][] result1 = obj.generateMatrix(1);
        System.out.println(Arrays.deepToString(result1));
        
        // Test case 2: A = 2
        int[][] result2 = obj.generateMatrix(2);
        System.out.println(Arrays.deepToString(result2));
        
        // Test case 3: A = 5
        int[][] result3 = obj.generateMatrix(5);
        System.out.println(Arrays.deepToString(result3));
    }
}