// The N queen puzzle is the problem of placing N queens on an N*N chessboard such that now two queens attack each other.
// Time complexity = O(1)
// Space complexity = O(n^2)

package DSA_Exercise.RecursionAndBacktracking;

public class NQueen2 {
    public static void main(String[] args){
        int n = 4;
        char[][] arr = new char[n][n];
        for (int i=0 ; i<arr.length ; i++){
            for(int j=0 ; j<arr.length; j++){
                arr[i][j] = '.' ;
            }
        }
        placeQueen(arr, 0, new boolean[n], new boolean[2 *n-1], new boolean[2 *n-1]);
    }

    public static void print(char[][] arr){
        for(int i=0 ; i<arr[0].length; i++){
            for(int j=0 ; j<arr[0].length ; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void placeQueen(char[][] arr, int row, boolean[] cols, boolean[] d1, boolean[] d2){
        if(row == arr.length){
            // decided for every row
            print(arr);
            System.out.println("-------------");
            return;
        }

        for(int col=0; col<arr[0].length; col++){
            if(cols[col] == false && d1[row + col] == false && d2[row - col + arr.length-1] == false){
                arr[row][col] = 'Q';
                cols[col] = true;
                d1[row + col] = true;
                d2[row - col + arr.length-1] = true;
                placeQueen(arr, row +1, cols, d1, d2);
                arr[row][col] = '.';
                cols[col] = false;
                d1[row + col] = false;
                d2[row - col + arr.length-1] = false;
            }
        }
    }
}