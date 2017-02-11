from collections import defaultdict
import random

random.seed(316351)
for a in range(0, 6):

    n = random.randint(50000, 55000)
    m = 25000
    weights1 = [i for i in range(2, n)]
    random.shuffle(weights1)
    weights = [0, 1] + weights1 + [n]
    inv = {weights[i]: i for i in range(1, n + 1)}
    adj1 = defaultdict(set)
    adj2 = defaultdict(set)
    for i in range(m):
        u = random.randint(1, n - 1)
        v = inv[random.randint(weights[u] + 1, n)]
        adj1[u].add(v)
        adj2[v].add(u)

    for i in range(2, n + 1):
        if len(adj2[i]) == 0:
            adj1[1].add(i)
            adj2[i].add(1)

    for i in range(1, n):
        if len(adj1[i]) == 0:
            adj1[i].add(n)
            adj2[n].add(i)

    edges = []
    for u, vs in adj1.items():
        for v in vs:
            edges.append((u, v))

    print n, len(edges)
    for u, v in edges:
        print u, v
