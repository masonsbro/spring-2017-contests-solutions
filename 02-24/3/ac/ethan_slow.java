import java.util.*;
import java.io.*;

public class ethan_slow {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        assert 1 <= t && t <= 10000;
        for (int q = 0; q < t; q++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            int c = scan.nextInt();
            int n = scan.nextInt();
            assert 1 <= a && a <= 12;
            assert 1 <= b && b <= 12;
            assert 1 <= c && c <= 12;
            assert 0 <= n && n <= 10000000;
            System.out.println(solve(a, b, c, n));
        }
    }

    private static long solve(int a, int b, int c, int n) {
        long cnt = 0;
        for (int i = 1; i <= n; i++) {
            cnt += i;
        }
        return 12L * a * b * c * cnt;
    }

}
