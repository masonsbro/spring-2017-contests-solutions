import java.util.*;
import java.io.*;

public class ethan_slowest {

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
        if (n == 0) return 1;
        if (n < 0) return 0;
        int ans = (solve(n - 1) + solve(n - 2)) % MOD;
        for (int i = 0; i < n; i++) {
            ans = (ans + solve(i)) % MOD;
        }
        return ans;
    }

}
