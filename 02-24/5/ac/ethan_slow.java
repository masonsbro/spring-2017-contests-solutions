import java.util.*;
import java.io.*;

public class ethan_slow {

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
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] = ((i >= 1 ? dp[i - 1] : 0) + (i >= 2 ? dp[i - 2] : 0)) % MOD;
            for (int j = 0; j < i; j++) {
                dp[i] = (dp[i] + dp[j]) % MOD;
            }
        }
        return dp[n];
    }

}
