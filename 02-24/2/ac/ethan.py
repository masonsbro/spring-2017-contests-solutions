t = int(raw_input())
for q in range(t):
    x, y = map(int, raw_input().split())
    points = [map(int, raw_input().split()) for i in range(int(raw_input()))]
    if len(points) == 0:
        print '(0,0)'
        continue
    best = (points[0][0], points[0][1])
    bestval = abs(points[0][0] - x) + abs(points[0][1] - y)
    for x1, y1 in points[1:]:
        if abs(x1 - x) + abs(y1 - y) < bestval:
            best = x1, y1
            bestval = abs(x1 - x) + abs(y1 - y)
    assert sum(map(lambda p: abs(p[0] - x) + abs(p[1] - y) == bestval, points)) == 1
    print '(%d,%d)' % best
