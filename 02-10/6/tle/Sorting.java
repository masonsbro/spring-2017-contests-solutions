import java.util.*;
import java.io.*;

public class Sorting {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int a = 0; a < cases; a++) {
			int commands = Integer.parseInt(br.readLine());
			HashMap<String, Node> map = new HashMap<String, Node>();
			boolean changed = false;
			TreeSet<Node> allNodes = new TreeSet<Node>();
			for (int b = 0; b < commands; b++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				String command = st.nextToken();
				if (command.equals("DELETE")) {
					if (map.size() == 0)
						sb.append("NONE\n");
					else {
						if (changed) {
							allNodes = new TreeSet<Node>();
							for (String s : map.keySet()) {
								allNodes.add(map.get(s));
							}
							changed = false;
						}
						map.remove(allNodes.first().getValue());
						sb.append(allNodes.first().getValue());
						allNodes.remove(allNodes.first());
						sb.append("\n");
					}
				} else {
					changed = true;
					String name = st.nextToken();
					if (map.containsKey(name)) {
						map.get(name).updateIndicator(b);
					} else {
						map.put(name, new Node(name, b));
					}
				}
			}
			sb.append('\n');
		}
		System.out.println(sb.toString());
	}

	private static class Node implements Comparable<Node> {
		private String value;
		private int indicator;

		public Node(String value, int indicator) {
			this.value = value;
			this.indicator = indicator;
		}

		public String getValue() {
			return this.value;
		}

		public void updateIndicator(int newIndicator) {
			this.indicator = newIndicator;
		}

		public int compareTo(Node other) {
			return other.indicator - this.indicator;
		}
	}
}