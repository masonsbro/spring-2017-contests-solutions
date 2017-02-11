from collections import defaultdict

t = int(raw_input())
for q in range(t):
    n, m = map(int, raw_input().split())
    edges = [map(int, raw_input().split()) for i in range(m)]
    adj = defaultdict(list)
    cnt = [0]*(n + 1)
    for u, v in edges:
        adj[u].append(v)
        cnt[v] += 1
    zero = [i for i in range(1, n + 1) if cnt[i] == 0]
    topo = []
    inv = {}
    while len(zero) > 0:
        cur = zero.pop()
        inv[cur] = len(topo)
        topo.append(cur)
        for v in adj[cur]:
            cnt[v] -= 1
            if cnt[v] == 0:
                zero.append(v)

    dp = [0]*n
    for i in range(n - 2, -1, -1):
        for v in adj[topo[i]]:
            dp[i] += 1.0 + dp[inv[v]]
        dp[i] *= 1.0 / len(adj[topo[i]])

    print "%0.3lf" % dp[0]
