import java.util.*;
import java.io.*;

public class Veronica {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		for (int a = 0; a < cases; a++) {
			int nums = Integer.parseInt(br.readLine());
			int result = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int c = 0; c < nums; c++) {
				if (Integer.bitCount(Integer.parseInt(st.nextToken())) % 2 == 1)
					result++;
			}
			System.out.println(result);
		}
	}
}