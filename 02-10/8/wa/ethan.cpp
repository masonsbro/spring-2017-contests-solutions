#include <cstdio>
#include <vector>
#include <cstdlib>

constexpr int MAX_N = 100005;
constexpr int TIMES = 1000;

using namespace std;

int t, n, m;
vector<int> adj[MAX_N];

int mc(int u) {
    if (u == n) return 0;
    return 1 + mc(adj[u][rand() % adj[u].size()]);
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

        double ans = 0;
        for (int i = 0; i < TIMES; i++) {
            ans += mc(1);
        }

        ans *= 1.0 / TIMES;

        printf("%0.3lf\n", ans);
    }

    return 0;
}
