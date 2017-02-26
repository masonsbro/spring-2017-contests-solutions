import java.util.*;
import java.io.*;

public class ethan {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int s = scan.nextInt();
        int t = scan.nextInt();
        assert 1 <= s && s <= 100000;
        assert 1 <= t && t <= 1000000000;
        int sum = 0;
        int[] ans = new int[s];
        for (int i = 0; i < s; i++) {
            int u = scan.nextInt();
            assert 1 <= u && u <= 1000000;
            ans[i] = t / u;
            sum += ans[i];
        }
        System.out.println(sum);
        for (int i = 0; i < s; i++) {
            System.out.printf("%d ", ans[i]);
        }
        System.out.println();
    }
}
