#include <cstdio>
#include <algorithm>

typedef long long ll;

constexpr int MAX_N = 1005;
constexpr int MAX_M = 2005;
constexpr int ZERO = MAX_M / 2;
constexpr int MOD = 1000000007;

using namespace std;

int t, n, m;
ll dp[MAX_N][MAX_M];

int main() {
    scanf(" %d %d", &n, &m);
    n--;
    dp[0][ZERO] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < MAX_M; j++) {
            for (int k = -1; k <= 1; k++) {
                if (j - k < 0 || j - k >= MAX_M) continue;
                dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % MOD;
            }
        }
    }
    printf("%lld\n", dp[n][ZERO+m]);

    return 0;
}
