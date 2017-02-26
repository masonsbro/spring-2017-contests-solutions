import java.util.*;

public class ethan_slow {

    private static final int MOD = 1000000007;

    private static final int MAX_M = 2005;
    private static final int ZERO = MAX_M / 2;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        System.out.println(solve(n - 1, m));
    }

    private static int solve(int n, int m) {
        int[][] dp = new int[n+1][MAX_M];
        dp[0][ZERO] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < MAX_M; j++) {
                for (int k = -1; k <= 1; k++) {
                    if (j - k < 0 || j - k >= MAX_M) continue;
                    dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % MOD;
                }
            }
        }

        return dp[n][ZERO+m];
    }

}
