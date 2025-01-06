// Give 2 strings A and B. Find the longest common subsequence, which is common in both the strings. You need to return the length of such longest common subsequence.
// Sample input
// A = "abbcdgf"
// B = "bbadcgf"
// Sample output 
// ans = 5
// Time complexity = O(n*m)
// space complexity = O(n*m)

package DSA_Exercise.DynamicProgramming;

public class LongestCommonSubseq {
    public static void main(String[] args){
        String a = "abbcdgf";
        String b = "bbadcgf";
        System.out.println(lcs(a,b,0,0, new int[a.length()][b.length()]));
        System.out.println(lcsTab(a,b));
    }

    public static int lcsTab(String s1, String s2){
        int [][] dp = new int[s1.length() + 1] [s2.length() + 1];
        for(int i=dp.length-2; i>=0; i--){
            for (int j= dp[0].length - 2; j>=0; j--){
                if(s1.charAt(i) == s2.charAt(j)){
                    dp[i][j] = 1+dp[i+1][j+1];
                }else{
                    dp[i][j] = Math.max(dp[i+1][j], dp[i][j+1]);
                }
            }
        }
        return dp[0][0];
    }

    public static int lcs(String s1, String s2, int i, int j, int[][] dp){
        if(i == s1.length() || j == s2.length()){
            return 0;
        }

        if(dp[i][j] != 0){
            return dp[i][j];
        }

        int ans = 0;
        if(s1.charAt(i) == s2.charAt(j)){
            ans = 1 + lcs(s1, s2, i+1, j+1, dp);
        } else{
            ans = Math.max(lcs(s1, s2, i, j+1, dp), lcs(s1, s2, i+1, j, dp));
        }

        dp[i][j] = ans;
        return ans;
    }
}
