import java.util.*;
import java.io.*;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int a = 0; a < cases; a++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int numFlights = Integer.parseInt(st.nextToken());
			int numRestrictions = Integer.parseInt(st.nextToken());
			int numTravelers = Integer.parseInt(st.nextToken());
			assert numFlights > 0 && numFlights <= 70000;
			assert numRestrictions >= 0 && numRestrictions <= 200;
			assert numTravelers >= 1 && numTravelers <= 500;
			HashMap<String, HashMap<String, Node>> graph = new HashMap<>();
			HashMap<String, HashSet<String>> noFly = new HashMap<>();
			for (int b = 0; b < numFlights; b++) {
				st = new StringTokenizer(br.readLine());
				String cityOne = st.nextToken();
				String countryOne = st.nextToken();
				st.nextToken();
				String cityTwo = st.nextToken();
				String countryTwo = st.nextToken();
				assert !cityOne.equals(cityTwo) || !countryOne.equals(countryTwo);
				insert(cityOne, countryOne, graph);
				insert(cityTwo, countryTwo, graph);
				graph.get(countryOne).get(cityOne).addConnection(graph.get(countryTwo).get(cityTwo));
				create(countryOne, noFly);
				create(countryTwo, noFly);
			}
			for (int b = 0; b < numRestrictions; b++) {
				st = new StringTokenizer(br.readLine());
				String countryOne = st.nextToken();
				st.nextToken();
				String countryTwo = st.nextToken();
				create(countryOne, noFly);
				create(countryTwo, noFly);
				noFly.get(countryOne).add(countryTwo);
			}
			for (int b = 0; b < numTravelers; b++) {
				st = new StringTokenizer(br.readLine());
				String nationality = st.nextToken();
				String startCity = st.nextToken();
				String startCountry = st.nextToken();
				st.nextToken();
				String endCity = st.nextToken();
				String endCountry = st.nextToken();

				assert !startCity.equals(endCity) || !startCountry.equals(endCountry);

				HashSet<String> thisNoFly = new HashSet<String>();
				if (noFly.containsKey(nationality)) 
					thisNoFly = noFly.get(nationality);
				int result;
				if (startCountry.equals(endCountry) && thisNoFly.contains(endCountry)) {
					if (!graph.containsKey(startCountry) || !graph.get(startCountry).containsKey(startCity))
						result = -1;
					else {
						result = travel(thisNoFly, graph.get(startCountry).get(startCity), 
							endCity, endCountry, true);
					}
				} else {
					if (!graph.containsKey(startCountry) || !graph.get(startCountry).containsKey(startCity)) {
						result = -1;
					} else {
						result = travel(thisNoFly, graph.get(startCountry).get(startCity),
												endCity, endCountry, false);
					}
				}
				if (result == -1)
					sb.append("IMPOSSIBLE");
				else
					sb.append(result);
				sb.append('\n');
			}
			sb.append('\n');
		}
		System.out.print(sb.toString());
	}

	private static int travel(HashSet<String> noFly, Node startNode, 
						String goalCity, String goalCountry, boolean domestic) {
		Queue<Node> toVisit = new LinkedList<Node>();
		HashMap<String, HashSet<String>> visited = new HashMap<>();
		int count = 0;
		Queue<Node> nextLevel = new LinkedList<Node>();
		toVisit.add(startNode);
		while (!toVisit.isEmpty()) {
			Node current = toVisit.remove();
			create(current.country, visited);
			if (visited.get(current.country).contains(current.city) 
				|| (domestic && !current.country.equals(goalCountry))
				|| (!domestic && noFly.contains(current.country)) && !current.country.equals(startNode.country)) {
				if (toVisit.isEmpty()) {
					toVisit = nextLevel;
					nextLevel = new LinkedList<Node>();
					count++;
				}
				continue;
			}
			visited.get(current.country).add(current.city);
			if (current.country.equals(goalCountry) && current.city.equals(goalCity))
				return count - 1;
			for (Node n : current.connections) {
				if (current.country.equals(n.country) || !noFly.contains(n.country))
					nextLevel.add(n);
			}
			if (toVisit.isEmpty()) {
				toVisit = nextLevel;
				nextLevel = new LinkedList<Node>();
				count++;
			}
		}
		return -1;
	}

	private static void create(String country, HashMap<String, HashSet<String>> list) {
		if (!list.containsKey(country)) {
			list.put(country, new HashSet<String>());
		}
	}

	private static void insert(String city, String country, HashMap<String, HashMap<String, Node>> graph) {
		if (!graph.containsKey(country)) {
			graph.put(country, new HashMap<String, Node>());
		}
		if (!graph.get(country).containsKey(city)) {
			graph.get(country).put(city, new Node(city, country));
		}
	}

	private static class Node {
		private String city;
		private String country;
		private ArrayList<Node> connections;

		public Node(String city, String country) {
			this.city = city;
			this.country = country;
			connections = new ArrayList<Node>();
		}

		public void addConnection(Node other) {
			connections.add(other);
		}
	}
}