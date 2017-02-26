from collections import defaultdict

n, m = map(int, raw_input().split())
adj = defaultdict(list)
cnt = defaultdict(lambda: 0)
for i in range(m):
    u, v = map(int, raw_input().split())
    adj[u].append(v)
    cnt[v] += 1

zero = []
num = 0

for u in range(1, n + 1):
    if cnt[u] == 0:
        zero.append(u)

while len(zero) > 0:
    u = zero.pop()
    num += 1
    for v in adj[u]:
        cnt[v] -= 1
        if cnt[v] == 0:
            zero.append(v)

if num == n:
    print "NO"
else:
    print "YES"
