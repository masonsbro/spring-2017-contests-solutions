MOD = 1000000007
MAX_M = 2005
ZERO = MAX_M / 2

def solve(n, m):
    dp = [[0 for i in range(MAX_M)] for j in range(n+1)]
    dp[0][ZERO] = 1
    for i in range(1, n + 1):
        for j in range(0, MAX_M):
            for k in range(-1, 2):
                if j - k < 0 or j - k >= MAX_M: continue
                dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % MOD
    return dp[n][ZERO+m]

n, m = map(int, raw_input().split())
print solve(n - 1, m)
