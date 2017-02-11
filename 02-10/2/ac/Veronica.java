import java.util.*;
import java.io.*;

public class Veronica {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		for (int a = 0; a < cases; a++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int numPassengers = Integer.parseInt(st.nextToken());
			int maxPassengers = Integer.parseInt(st.nextToken());
			ArrayList<Long> costs = new ArrayList<Long>();
			st = new StringTokenizer(br.readLine());
			for (int b = 0; b < numPassengers; b++) {
				costs.add(Long.parseLong(st.nextToken()));
			}
			long result = 0;
			int numToRemove = Math.max(0, numPassengers - maxPassengers);
			Collections.sort(costs);
			for (int b = 0; b < numToRemove; b++) {
				result += costs.get(b);
			}
			System.out.println(result);
		}
	}
}