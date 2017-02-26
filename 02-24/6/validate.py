n, m = map(int, raw_input().split())
edges = [map(int, raw_input().split()) for i in range(m)]
edges = [(p[0], p[1]) for p in edges]

if len(set(edges)) != len(edges):
    print 'multiple edges'
if any(map(lambda edge: edge[0] == edge[1], edges)):
    print 'self-loops'
