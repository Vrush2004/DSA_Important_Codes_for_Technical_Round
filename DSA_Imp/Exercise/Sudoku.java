// Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.' You may assume that there will be only one unique solution.

package DSA_Imp.Exercise;

import java.util.ArrayList;

public class Sudoku {

    public void solveSudoku(ArrayList<ArrayList<Character>> board) {
        solve(board);
    }

    // Backtracking approach to solve Sudoku
    private boolean solve(ArrayList<ArrayList<Character>> board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board.get(row).get(col) == '.') {  // Find empty cell
                    for (char num = '1'; num <= '9'; num++) {  // Try digits from 1 to 9
                        if (isValid(board, row, col, num)) {
                            board.get(row).set(col, num);  // Try this number
                            if (solve(board)) {  // Recursively try to solve
                                return true;
                            }
                            board.get(row).set(col, '.');  // Backtrack if no solution
                        }
                    }
                    return false;  // If no valid number can be placed, return false
                }
            }
        }
        return true;  // Puzzle solved
    }

    // Check if placing num at board[row][col] is valid
    private boolean isValid(ArrayList<ArrayList<Character>> board, int row, int col, char num) {
        // Check row
        for (int i = 0; i < 9; i++) {
            if (board.get(row).get(i) == num) {
                return false;
            }
        }
        
        // Check column
        for (int i = 0; i < 9; i++) {
            if (board.get(i).get(col) == num) {
                return false;
            }
        }
        
        // Check 3x3 subgrid
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                if (board.get(i).get(j) == num) {
                    return false;
                }
            }
        }
        
        return true;
    }

    // Main method to test the Sudoku solver
    public static void main(String[] args) {
        ArrayList<ArrayList<Character>> board = new ArrayList<>();

        // Initialize the board with a sample puzzle
        char[][] initialBoard = {
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

        // Convert initialBoard to ArrayList<ArrayList<Character>>
        for (char[] row : initialBoard) {
            ArrayList<Character> boardRow = new ArrayList<>();
            for (char c : row) {
                boardRow.add(c);
            }
            board.add(boardRow);
        }

        // Solve the Sudoku puzzle
        Sudoku sudokuSolver = new Sudoku();
        sudokuSolver.solveSudoku(board);

        // Print the solved board
        for (ArrayList<Character> row : board) {
            for (char c : row) {
                System.out.print(c + " ");
            }
            System.out.println();
        }
    }
}