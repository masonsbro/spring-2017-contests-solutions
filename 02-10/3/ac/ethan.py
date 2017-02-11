t = int(raw_input())
for q in range(t):
    n = int(raw_input())
    x = map(int, raw_input().split())
    print sum(map(lambda y: bin(y).count('1') & 1, x))
