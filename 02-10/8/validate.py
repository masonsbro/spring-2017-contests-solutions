from collections import defaultdict

def in_bounds(n, m, edges, adj1, adj2):
    return 1 <= n <= 100000 and 1 <= m <= 100000

def can_reach(n, m, edges, adj1, adj2):
    s = [1]
    vis = set()
    while len(s) > 0:
        cur = s.pop()
        if cur == n: return True
        if cur in vis: continue
        vis.add(cur)
        for v in adj1[cur]:
            s.append(v)
    return False

def no_cycles(n, m, edges, adj1, adj2):
    cnt = {u: len(adj2[u]) for u in range(1, n + 1)}
    zero = [u for u in range(1, n + 1) if cnt[u] == 0]
    s = []
    while len(zero) > 0:
        cur = zero.pop()
        s.append(cur)
        for v in adj1[cur]:
            cnt[v] -= 1
            if cnt[v] == 0:
                zero.append(v)
    return len(s) == n

def reach(n, m, adj, start):
    s = [start]
    vis = set()
    while len(s) > 0:
        cur = s.pop()
        if cur in vis: continue
        vis.add(cur)
        for v in adj[cur]:
            s.append(v)
    return vis

def no_useless_edges(n, m, edges, adj1, adj2):
    reach1 = reach(n, m, adj1, 1)
    reach2 = reach(n, m, adj2, n)
    if len(reach1) != len(reach2) or len(reach1) != n:
        return False
    for u, v in edges:
        if u not in reach1 or v not in reach2:
            return False
    return True

def no_duplicate_edges(n, m, edges, adj1, adj2):
    edges = map(lambda x: (x[0], x[1]), edges)
    return len(edges) == len(set(edges))

checks = {
    in_bounds: "n, m not in bounds",
    can_reach: "cannot reach N from 1",
    no_cycles: "there's a cycle",
    no_useless_edges: "there are edges that are not part of a path from 1 to N",
    no_duplicate_edges: "there are duplicate edges"
}

t = int(raw_input())
if t < 1 or t > 10: print "wrong number of tests"
for q in range(t):
    print "on test %d" % (q + 1)
    n, m = map(int, raw_input().split())
    edges = [map(int, raw_input().split()) for i in range(m)]
    adj1 = defaultdict(list)
    adj2 = defaultdict(list)
    for u, v in edges:
        adj1[u].append(v)
        adj2[v].append(u)
    for f, msg in checks.iteritems():
        if not f(n, m, edges, adj1, adj2):
            print "test %d: %s" % (q + 1, msg)

try:
    raw_input()
    print "too much input"
except:
    pass
