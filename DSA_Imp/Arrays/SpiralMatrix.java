// Give a matrix N*M. print all the elements of matrix in spiral order.
// input
// {{1,2,3,4},
//  {5,6,7,8},
//  {9,10,11,12},
//  {13,14,15,16}}
// Output = {1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10}
// Time complexity = O(n*m) 
// Space complexity = O(1)

package DSA_Imp.Arrays;

public class SpiralMatrix {
    public static void main(String[] args){
        int[][] arr ={{1,2,3,4,5},
                      {6,7,8,9,10},
                      {11,12,13,14,15}};
        matrix(arr);
    }
    public static void matrix(int[][] arr){
        int n = arr.length;
        int m = arr[0].length;
        int rmin = 0, rmax=arr.length-1;
        int cmin = 0, cmax= arr[0].length-1;
        int count =0;
        while(count < n * m){
            // top boundary
            for(int col = cmin; col <= cmax && count< n*m; col++){
                System.out.print(arr[rmin][col] + " ");
                count++;
            }
            rmin++;

            // rignt boundary
            for(int row = rmin; row <= rmax && count< n*m; row++){
                System.out.print(arr[row][cmax] + " ");
                count++;
            }
            cmax--;

            // bottom boundary
            for(int col = cmax; col >= cmin && count< n*m; col--){
                System.out.print(arr[rmax][col] + " ");
                count++;
            }
            rmax--;

            // left boundary
            for(int row = rmax; row >= rmin && count< n*m; row--){
                System.out.print(arr[row][cmin] + " ");
                count++;
            }
            cmin++;
        } 
    }
}