#include <cstdio>
#include <vector>
#include <cstring>

constexpr int MAX_N = 100005;

using namespace std;

int t, n, m;
vector<int> adj[MAX_N];

double dfs(int u) {
    if (u == n) return 0;
    double ans = 0;
    for (int v : adj[u]) {
        ans += 1 + dfs(v);
    }
    ans *= 1.0 / adj[u].size();
    return ans;
}

int main() {
    scanf(" %d", &t);
    for (int q = 0; q < t; q++) {
        scanf(" %d %d", &n, &m);
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
