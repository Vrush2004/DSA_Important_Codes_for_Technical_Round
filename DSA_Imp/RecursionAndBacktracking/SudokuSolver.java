package DSA_Imp.RecursionAndBacktracking;

public class SudokuSolver {
    public static void solveSudoku(char[][] arr){
        if(sudoku(arr, 0, 0)){
            for(int i =0; i<arr.length; i++){
                for(int j =0; j<arr[0].length; i++){
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

        if(arr[i][j] == '.'){
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
    }
}