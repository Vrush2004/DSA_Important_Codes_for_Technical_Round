package DSA_Imp.Graphs;

public class ColoringABorder {
    public static void main(String[] args){

    }

    public static int[][] colorBorder(int[][] arr, int row, int col, int color){
        int oc = arr[row][col];
        dfs(arr, row, col, oc);
    }

    public static void dfs(int[][] arr, int r, int c, int oc){
        if(r < 0 || c < 0 || r >= arr.length || c >= arr[0].length || arr[r][c] != oc){
            return;
        }

        arr[r][c] = -oc;
        // top
        dfs(arr, r - 1, c, oc);
        // left
        dfs(arr, r, c - 1, oc);
        // down
        dfs(arr, r + 1, c, oc);
        // right
        dfs(arr, r, c + 1, oc);

        if(r - 1 >= 0 && col - 1 >= 0){
            
        }
    }
}