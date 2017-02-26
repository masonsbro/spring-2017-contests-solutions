#include <cstdio>
#include <cassert>

typedef long long ll;

constexpr int MAX_FACT = 1000005;
constexpr int MOD = 1000000007;

using namespace std;

int t, n, m;
ll fact[MAX_FACT];

int mod_inv(int a) {
    ll m = MOD, t, q;
    ll x0 = 0, x1 = 1;

    while (a > 1) {
        q = a / m;
        t = m;
        m = a % m, a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    if (x1 < 0) {
        x1 += MOD;
    }

    return x1;
}

int comb(int a, int b) {
    if (a < 0 || b < 0 || b > a) {
        return 0;
    } else {
        return ((fact[a] * mod_inv(fact[b])) % MOD) * mod_inv(fact[a-b]) % MOD;
    }
}

int main() {
    fact[0] = 1;
    for (int i = 1; i < MAX_FACT; i++) {
        fact[i] = (i * fact[i-1]) % MOD;
    }

    scanf(" %d %d", &n, &m);
    n--;
    
    ll ans = 0;
    for (int k = 0; k <= n; k++) {
        ll cur = ((ll) comb(n, k) * comb(n - k, m + k)) % MOD;
        ans = (ans + cur) % MOD;
    }

    printf("%lld\n", ans);

    return 0;
}
