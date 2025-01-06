// Give a positive number N. You need to find the smallest number S such that product of digits of S is equal to N.
// Sample input 
// N=1000
// Sample output = 5558
// Time complexity= 0(log2n)
// space complexity= O(1)

package DSA_Exercise.Arrays;
import java.util.*;

public class SmallestNum {
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        System.out.println(solution(n));
    }
    public static int solution(int n){
        String ans ="";
        for(int div = 9 ; div >= 2; div--){
            while(n%div ==0){
                n=n/div;
                ans = div + ans;
            }
        }
        if(n != 1){
            return -1;
        }else{
            return Integer.parseInt(ans);
        }
    }
}
