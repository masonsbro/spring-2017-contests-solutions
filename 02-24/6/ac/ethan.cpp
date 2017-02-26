#include <cstdio>
#include <vector>

constexpr int MAX_N = 100100;

using namespace std;

int n, m;
vector<int> adj[MAX_N];

bool vis1[MAX_N];
bool vis2[MAX_N];

bool dfs(int u) {
    if (vis1[u]) return true;
    if (vis2[u]) return false;
    vis1[u] = true;
    bool ans = false;
    for (int v : adj[u]) {
        ans |= dfs(v);
    }
    vis1[u] = false;
    vis2[u] = true;
    return ans;
}

int main() {
    scanf(" %d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf(" %d %d", &u, &v);
        adj[u].push_back(v);
    }

    bool ans = false;
    for (int i = 1; i <= n; i++) {
        ans |= dfs(i);
    }

    if (ans) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
