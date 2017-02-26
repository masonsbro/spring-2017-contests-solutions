t = int(input())
for i in range(t):
    c,g = map(int, input().split())
    print("LEFT") if c > g else print("RIGHT")
