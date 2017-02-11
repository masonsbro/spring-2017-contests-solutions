import java.util.*;
import java.io.*;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int a = 0; a < cases; a++) {
			int interactions = Integer.parseInt(br.readLine());
			Buffer other = new Buffer();
			for (int b = 0; b < interactions; b++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				String command = st.nextToken();
				if (command.equals("SEND") || command.equals("RECEIVE")) {
					String name = st.nextToken();
					if (other.contains(name))
						other.remove(name);
					other.addFront(name);
				} else if (command.equals("DELETE")) {
					String result = other.removeFront();
					if (result == null)
						sb.append("NONE\n");
					else {
						sb.append(result);
						sb.append('\n');
					}
				} else {
					throw new IllegalArgumentException("Didn't recognize command. " + command);
				}
			}
			sb.append('\n');
		}
		System.out.print(sb.toString());
	}

	private static class Buffer {

		private static class Node {
			private Node previous;
			private Node next;
			private String value;

			public Node(Node previous, Node next, String value) {
				this.previous =  previous;
				this.next = next;
				this.value = value;
			}
		}

		private Node head;
		private Node tail;
		HashMap<String, Node> map;

		public Buffer() {
			head = new Node(null, null, null);
			tail = new Node(null, null, null);
			head.next = tail;
			tail.previous = head;
			map = new HashMap<String, Node>();
		}

		public boolean contains(String name) {
			return map.containsKey(name);
		}

		public void remove(String name) {
			Node tgt = map.get(name);
			tgt.next.previous = tgt.previous;
			tgt.previous.next = tgt.next;
			map.remove(name);
		}

		public String removeFront() {
			if (head.next == tail)
				return null;
			String toRemove = head.next.value;
			remove(toRemove);
			return toRemove;
		}

		public void addFront(String name) {
			Node n = new Node(head, head.next, name);
			n.next.previous = n;
			head.next = n;
			map.put(name, n);
		}

		// DEBUGGING PURPOSES ONLY
		public String getPrint() {
			StringBuilder sb = new StringBuilder();
			Node curr = head.next;
			while (curr != tail) {
				sb.append(curr.value);
				curr = curr.next;
				sb.append('\n');
			}
			return sb.toString();
		}
	}
}