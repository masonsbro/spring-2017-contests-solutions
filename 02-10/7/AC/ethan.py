from collections import defaultdict, deque

def parse_flight(s):
    s = s.split()
    return ((s[0], s[1]), (s[3], s[4]))

def parse_restriction(s):
    s = s.split()
    return (s[0], s[2])

def parse_query(s):
    s = s.split()
    return (s[0], (s[1], s[2]), (s[4], s[5]))

t = int(raw_input())

for q in range(t):
    n, m, p = map(int, raw_input().split())
    flights = map(parse_flight, [raw_input() for i in range(n)])
    restrictions = set(map(parse_restriction, [raw_input() for i in range(m)]))
    adj = defaultdict(list)
    for flight in flights:
        adj[flight[0]].append(flight[1])
    for i in range(p):
        home, start, end = parse_query(raw_input())
        to_visit = deque([start])
        visited = set()
        depth = 0
        ans = None
        while len(to_visit) > 0:
            sz = len(to_visit)
            for j in range(sz):
                cur = to_visit.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                if cur == end:
                    ans = depth
                    break
                for v in adj[cur]:
                    if v[1] == cur[1] or (home, v[1]) not in restrictions:
                        to_visit.append(v)
            if ans is not None: break
            depth += 1
        print ans - 1 if ans is not None else "IMPOSSIBLE"
    print
