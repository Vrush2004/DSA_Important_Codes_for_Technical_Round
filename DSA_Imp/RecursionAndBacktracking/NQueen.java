// The N queen puzzle is the problem of placing N queens on an N*N chessboard such that now two queens attack each other.
// Time complexity = O(n*n!)
// Space complexity = O(n^2)

package DSA_Imp.RecursionAndBacktracking;

public class NQueen {
    public static void main(String[] args){
        int n = 4;
        char[][] arr = new char[n][n];
        for (int i=0 ; i<arr.length ; i++){
            for(int j=0 ; j<arr.length; j++){
                arr[i][j] = '.' ;
            }
        }
        placeQueen(arr, 0);
    }

    public static void print(char[][] arr){
        for(int i=0 ; i<arr[0].length; i++){
            for(int j=0 ; j<arr[0].length ; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static boolean isSafe(char[][] arr, int row, int col){
        for(int i =0; i<row; i++){
            if (arr[i][col] == 'Q'){
                return false;
            }
        }

        for(int i = row-1, j=col+1; i>=0 && j<arr[0].length; i--,j++){
            if(arr[i][j] == 'Q'){
                return false;
            }
        }

        for(int i = row-1, j=col-1; i>=0 && j>=0; i--,j--){
            if(arr[i][j] == 'Q'){
                return false;
            }
        }

        return true;
    }

    public static void placeQueen(char[][] arr, int row){
        if(row == arr.length){
            // decided for every row
            print(arr);
            System.out.println("-------------");
            return;
        }

        for(int col=0; col<arr[0].length; col++){
            if(isSafe(arr, row, col) == true){
                arr[row][col] = 'Q';
                placeQueen(arr, row +1);
                arr[row][col] = '.';
            }
        }
    }
}