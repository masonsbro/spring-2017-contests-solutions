#include <cstdio>
#include <vector>
#include <cstring>

constexpr int MAX_N = 100005;

using namespace std;

int t, n, m;
vector<int> adj[MAX_N];

int inv[MAX_N];
int cnt[MAX_N];

double dp[MAX_N];

int main() {
    scanf(" %d", &t);
    for (int q = 0; q < t; q++) {
        scanf(" %d %d", &n, &m);
        memset(cnt, 0, sizeof(cnt));
        for (int i = 1; i <= n; i++) {
            adj[i].clear();
        }
        for (int i = 0; i < m; i++) {
            int u, v;
            scanf(" %d %d", &u, &v);
            adj[u].push_back(v);
            cnt[v]++;
        }

        vector<int> zero;
        for (int i = 1; i <= n; i++) {
            if (cnt[i] == 0) zero.push_back(i);
        }

        vector<int> sorted;
        for (int i = 0; i < n; i++) {
            int cur = zero.back(); zero.pop_back();
            inv[cur] = sorted.size();
            sorted.push_back(cur);
            for (int v : adj[cur]) {
                if (--cnt[v] == 0) {
                    zero.push_back(v);
                }
            }
        }

        dp[n - 1] = 0;
        for (int i = n - 2; i >= 0; i--) {
            dp[i] = 0;
            for (int v : adj[sorted[i]]) {
                dp[i] += 1 + dp[inv[v]];
            }
            dp[i] *= 1.0 / adj[sorted[i]].size();
        }
        
        printf("%0.3lf\n", dp[0]);
    }
    
    return 0;
}
