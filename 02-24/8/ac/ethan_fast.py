MAX_FACT = 1000005
MOD = 1000000007

fact = [0]*MAX_FACT
fact[0] = 1
for i in range(1, MAX_FACT):
    fact[i] = (i * fact[i-1]) % MOD

def mod_inv(a):
    return pow(a, MOD - 2, MOD)

def comb(a, b):
    if a < 0 or b < 0 or b > a:
        return 0
    else:
        return ((fact[a] * mod_inv(fact[b])) % MOD) * mod_inv(fact[a-b]) % MOD

def solve(n, m):
    ans = 0
    for k in range(0, n + 1):
        cur = (comb(n, k) * comb(n - k, m + k)) % MOD
        ans = (ans + cur) % MOD
    return ans

n, m = map(int, raw_input().split())
print solve(n - 1, m)
