// The N-queens puzzle is the problem of placing N queens on an N×N chessboard such that no two queens attack each other.

package DSA_Imp.Exercise;
import java.util.ArrayList;

public class NQueen {
    public ArrayList<ArrayList<String>> solveNQueens(int A) {
        ArrayList<ArrayList<String>> solutions = new ArrayList<>();
        int[] board = new int[A]; // This will store the column index for each row
        solve(solutions, board, 0, A);
        return solutions;
    }

    // Backtracking method to solve the puzzle
    private void solve(ArrayList<ArrayList<String>> solutions, int[] board, int row, int n) {
        if (row == n) { // If we've placed queens in all rows, it's a valid solution
            ArrayList<String> solution = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                char[] rowString = new char[n];
                for (int j = 0; j < n; j++) {
                    if (board[i] == j) {
                        rowString[j] = 'Q'; // Place queen
                    } else {
                        rowString[j] = '.'; // Empty cell
                    }
                }
                solution.add(new String(rowString)); // Add the row to the solution
            }
            solutions.add(solution);
            return;
        }

        // Try placing a queen in all columns of the current row
        for (int col = n - 1; col >= 0; col--) { // Iterate in reverse for reverse lexicographical order
            if (isSafe(board, row, col, n)) {
                board[row] = col; // Place queen
                solve(solutions, board, row + 1, n); // Try to place a queen in the next row
                board[row] = -1; // Backtrack
            }
        }
    }

    // Check if it's safe to place a queen at (row, col)
    private boolean isSafe(int[] board, int row, int col, int n) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || Math.abs(board[i] - col) == Math.abs(i - row)) {
                return false; // Check if same column or same diagonal
            }
        }
        return true;
    }
}