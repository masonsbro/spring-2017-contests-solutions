import java.util.*;
import java.io.*;

public class Veronica {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		for (int a = 0; a < cases; a++) {
			String seat = br.readLine();
			int seatNum = Integer.parseInt(seat.substring(0, seat.length() - 1));
			System.out.println(seatNum * 6L);
		}
	}
}