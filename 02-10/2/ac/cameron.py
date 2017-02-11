def solve(passengers_to_bribe, prices):
    prices.sort()
    last_price = -1
    bribe_cost = 0
    index = 0
    while passengers_to_bribe > 0:
        bribe_cost += prices[index]
        index += 1
        passengers_to_bribe -= 1
        
    return bribe_cost

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    prices = list(map(int, input().split()))
    print(solve(n - m, prices))
