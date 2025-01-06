// Time Complexity = O(9^m)
// Space complexity = O(n^2)

package DSA_Exercise.RecursionAndBacktracking;

public class SudokuSolver {
    public static void main(String[] args){
        char[][] board = {
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        
        // Solve the Sudoku puzzle and print the result
        solveSudoku(board);
    }

    public static void solveSudoku(char[][] arr){
        if(sudoku(arr, 0, 0)){
            for(int i =0; i<arr.length; i++){
                for(int j =0; j<arr[0].length; j++){
                    System.out.print(arr[i][j] + " ");
                }
                System.out.println();
            }
        }
    }
    public static boolean sudoku(char[][] arr, int x, int y){
        if(x == arr.length){
            return true;
        }

        int nx = y == 8 ? x+1:x;
        int ny = y == 8 ? 0:y+1;

        if(arr[x][y] == '.'){
            for(int val = 1; val <= 9; val++){
                if(canWePlace(arr, x, y, val) == true){
                    arr[x][y] = (char)(val + '0');
                    if(sudoku(arr, nx, ny)){
                        return true;
                    }
                    arr[x][y] = '.';
                }
            }
        }else{
            if(sudoku(arr, nx, ny) == true){
                return true;
            }
        }
        return false;
    }
    public static boolean canWePlace(char[][] arr, int x, int y, int val){
        // check the row
        for(int col = 0; col<arr[0].length; col++){
            if(arr[x][col] == (char)(val + '0')){
                return false;
            }
        }

        // Check the column
        for(int row = 0; row<arr.length; row++){
            if(arr[row][y] == (char)(val + '0')){
                return false;
            }
        }

        // check the 3*3 grid
        x = x- (x % 3);
        y = y- (y % 3);

        for(int i =0; i<2; i++){
            for(int j = 0; j<2; j++){
                if(arr[x+i][y+j] == (char)(val + '0')){
                    return false;
                }
            }
        }
        return true;
    }
}