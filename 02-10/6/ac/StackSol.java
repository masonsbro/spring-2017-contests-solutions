import java.util.*;
import java.io.*;

public class StackSol {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int a = 0; a < cases; a++) {
			HashSet<String> currentViable = new HashSet<String>();
			Stack<String> communications = new Stack<String>();
			int interactions = Integer.parseInt(br.readLine());
			for (int b = 0; b < interactions; b++) {
				String line = br.readLine();
				if (line.equals("DELETE")) {
					boolean done = false;
					while (!done) {
						if (currentViable.size() == 0) {
							sb.append("NONE\n");
							done = true;
						} else {
							String possibility = communications.pop();
							if (currentViable.contains(possibility)) {
								sb.append(possibility);
								sb.append("\n");
								currentViable.remove(possibility);
								done = true;
							}
						}
					}
				} else {
					StringTokenizer st = new StringTokenizer(line);
					st.nextToken();
					String name = st.nextToken();
					communications.push(name);
					currentViable.add(name);
				}
			}
			sb.append("\n");
		}
		System.out.print(sb.toString());
	}
}