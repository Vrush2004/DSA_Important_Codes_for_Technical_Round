// time complexity = O(n^2)
// space complexity = O(n^2)

package DSA_Exercise.Graphs;

public class ColoringABorder {
    public static void main(String[] args){
        int[][] arr = {{2,3,4,3,1}, {4,2,2,2,1}, {1,2,2,2,1},{5,2,2,2,1}, {6,7,8,1,0}};
        colorBorder(arr, 1, 1, 3);
        for(int i = 0; i< arr.length; i++){
            for(int j = 0; j< arr[0].length; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int[][] colorBorder(int[][] arr, int row, int col, int color){
        int oc = arr[row][col];
        dfs(arr, row, col, oc);
        for(int i = 0; i< arr.length; i++){
            for(int j = 0; j< arr[0].length; j++){
                if(arr[i][j] < 0){
                    arr[i][j] = color;
                }
            }
        }
        return arr;
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

        if(r - 1 >= 0 && c - 1 >= 0 && r + 1 < arr.length && c + 1 < arr[0].length && 
            Math.abs(arr[r - 1][c]) == oc && 
            Math.abs(arr[r + 1][c]) == oc &&
            Math.abs(arr[r][c - 1]) == oc &&
            Math.abs(arr[r][c + 1]) == oc){
                // this element arr[r][c], is not a boundary element
                arr[r][c] = oc;
            }   
    }
}