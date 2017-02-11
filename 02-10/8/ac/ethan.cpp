#include <cstdio>
#include <vector>
#include <cstring>

constexpr int MAX_N = 100005;

using namespace std;

int t, n, m;
vector<int> adj[MAX_N];

bool visited[MAX_N];
double dp[MAX_N];

double dfs(int u) {
    if (u == n) return 0;
    if (visited[u]) return dp[u];
    visited[u] = true;
    dp[u] = 0;
    for (int v : adj[u]) {
        dp[u] += 1 + dfs(v);
    }
    dp[u] *= 1.0 / adj[u].size();
    return dp[u];
}

int main() {
    scanf(" %d", &t);
    for (int q = 0; q < t; q++) {
        scanf(" %d %d", &n, &m);
        memset(visited, 0, sizeof(visited));
        for (int i = 1; i <= n; i++) {
            adj[i].clear();
        }
        for (int i = 0; i < m; i++) {
            int u, v;
            scanf(" %d %d", &u, &v);
            adj[u].push_back(v);
        }
        printf("%0.3lf\n", dfs(1));
    }

    return 0;
}
