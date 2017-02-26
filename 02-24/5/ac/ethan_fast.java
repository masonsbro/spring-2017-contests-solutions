import java.util.*;
import java.io.*;

public class ethan_fast {

    private static final int MOD = 1000000007;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for (int q = 0; q < t; q++) {
            int n = scan.nextInt();
            System.out.println(solve(n));
        }
    }

    private static int solve(int n) {
        int[] dp = new int[n + 1];
        int sum = 1;
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] = ((i >= 1 ? dp[i - 1] : 0) + (i >= 2 ? dp[i - 2] : 0)) % MOD;
            dp[i] = (dp[i] + sum) % MOD;
            sum = (sum + dp[i]) % MOD;
        }
        return dp[n];
    }

}
