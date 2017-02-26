import java.util.*;

public class ethan_fast {

    private static final int MAX_FACT = 1000005;
    private static final int MOD = 1000000007;

    private static int[] fact = new int[MAX_FACT];

    public static void main(String[] args) {
        computeFactorials();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        System.out.println(solve(n - 1, m));
    }

    private static void computeFactorials() {
        fact[0] = 1;
        for (int i = 1; i < MAX_FACT; i++) {
            fact[i] = (int) (((long) i * fact[i-1]) % MOD);
        }
    }

    private static int solve(int n, int m) {
        long ans = 0;
        for (int k = 0; k <= n; k++) {
            long cur = ((long) comb(n, k) * comb(n - k, m + k)) % MOD;
            ans = (ans + cur) % MOD;
        }

        return (int) ans;
    }

    private static int comb(int a, int b) {
        if (a < 0 || b < 0 || b > a) {
            return 0;
        } else {
            return (int) (((long) fact[a] * modInv(fact[b]) % MOD) * modInv(fact[a-b]) % MOD);
        }
    }

    private static int modInv(long a) {
        long m = MOD, x0 = 0, x1 = 1;

        while (a > 1) {
            long q = a / m;
            long t = m;
            m = a % m;
            a = t;
            t = x0;
            x0 = x1 - q * x0;
            x1 = t;
        }

        if (x1 < 0) {
            x1 += MOD;
        }

        return (int) x1;
    }

}
