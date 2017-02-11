from collections import defaultdict
from queue import deque

def get_flight(flight):
    return ((flight[0], flight[1]), (flight[3], flight[4]))

def get_restriction(restriction):
    return ((restriction[0], restriction[2]))

def get_trip(trip):
    return (trip[0]), (trip[1], trip[2]), (trip[4], trip[5])



def bfs(nationality, start, end, adj, restrictions):
    q = deque()
    q.append(start)
    level = 0
    visited = set()
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node in visited:
                continue
            if node == end:
                return level - 1
            visited.add(node)
            for n in adj[node]:
                if (nationality, n[1]) not in restrictions or n[1] == node[1]:
                    q.append(n)
        level += 1
    return "IMPOSSIBLE"


t = int(input())
for i in range(t):
    f, r, q = map(int, input().split())
    flights = []
    restrictions = []
    for j in range(f):
        flights.append(get_flight(input().split()))
    for j in range(r):
        restrictions.append(get_restriction(input().split()))
    adj = defaultdict(list)
    for flight in flights:
        adj[flight[0]].append(flight[1])
    for j in range(q):
        nationality, start, end = get_trip(input().split())
        print(bfs(nationality, start, end, adj, restrictions))
    print()