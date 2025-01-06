// Given an array of points, where points[i] represents a point on XY plane, and an integer K. You need to return the Kclosest points to the origin(0,0)
// Sample input 
// arr = {{3,3}, {5,-1}, {-2,4}}
// k= 2
// Sample output = {{-2,4},{3,3}}
// Time complexity = O(nlogk)
// Space complexity = O(k)

package DSA_Exercise.Heap;
import java.util.*;

public class KClosestPointsToOrigin{
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        int[][] arr = new int[6][2];
        for(int i = 0; i< 6; i++){
            arr[i][0] = scn.nextInt();
            arr[i][1] = scn.nextInt();
        }
        int[][] ans = kClosestPoints(arr, 3);
        for(int[] a : ans){
            System.out.println("{" + a[0] + " " + a[1] + "} ");
        }
    }

    public static int[][] kClosestPoints(int[][] arr, int k){
        PriorityQueue<int[]> pq = new PriorityQueue<>((p1,p2) -> p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1]);

        int[][]ans = new int[k][2];

        for(int i = 0; i<arr.length; i++){
            pq.add(arr[i]);
            if(pq.size() > k){
                pq.remove();
            }
        }

        for(int i = 0; i<k; i++){
            ans[i] = pq.remove();
        }
        return ans;
    }
}