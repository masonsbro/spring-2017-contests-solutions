def solve_fast(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 2
    rail_sum = dp[0] + dp[1]
    for i in range(2,n+1):
        dp[i] = (rail_sum + dp[i-1] + dp[i-2]) % 1000000007
        rail_sum = (rail_sum + dp[i]) % 1000000007
    return dp[n] % 1000000007


def solve_fast_memo(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if n in memo:
        return memo[n]

    num_ways_from_n = 0

    for i in range(0, n):
        num_ways_from_n = (num_ways_from_n + solve_fast_memo(i,memo)) % 1000000007

    num_ways_from_n = (num_ways_from_n + solve_fast_memo(n-1,memo) + solve_fast_memo(n-2,memo)) % 1000000007

    memo[n] = num_ways_from_n

    return num_ways_from_n % 1000000007

def solve_slow(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    num_ways_from_n = 0

    for i in range(0, n):
        num_ways_from_n += solve_slow(i)

    num_ways_from_n += solve_slow(n-1) + solve_slow(n-2)

    return num_ways_from_n % 1000000007

t = int(input())
for i in range(t):
    n = int(input())
    print(solve_fast(n))