#include <cstdio>

using namespace std;

const int MAXN = 1000006;
const int MOD = 1000000007;

int fact[MAXN];
int tcaf[MAXN];

inline int sum(int a, int b) {
    int c = a + b;
    if (c >= MOD) {
        c -= MOD;
    }

    return c;
}

inline int prod(int a, int b) {
    return (1LL * a * b) % MOD;
}

int modpow(int base, int exp) {
    int cur = base;
    int res = 1;
    for (int p = 1; p <= exp; p <<= 1) {
        if (p & exp) {
            res = prod(res, cur);
        }

        cur = prod(cur, cur);
    }

    return res;
}

void gen_fact() {
    fact[0] = tcaf[0] = 1;
    for (int i = 1; i < MAXN; ++i) {
        fact[i] = prod(i, fact[i - 1]);
        tcaf[i] = modpow(fact[i], MOD - 2);
    }
}

int choose(int n, int k) {
    if (k > n or k < 0) return 0;

    return prod(fact[n], prod(tcaf[k], tcaf[n - k]));
}

int main() {
    gen_fact();

    int n, m;
    scanf("%d %d", &n, &m);

    // There are n - 1 slots
    // Each slot is -1, 0, 1
    // sum of slots needs to equal m
    // say we fix that there are k -1s
    // Then there must be k + m 1s
    // Then there are (n - 1, k) * (n - 1 - k, k + m) combos

    int ans = 0;
    for (int k = 0; k <= n - 1; ++k) {
        ans = sum(ans, prod(choose(n - 1, k), choose(n - 1 - k, k + m)));
    }

    printf("%d\n", ans);

    return 0;
}
