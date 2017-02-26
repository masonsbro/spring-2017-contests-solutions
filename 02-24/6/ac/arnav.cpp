#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

const int MAXN = 100005;
int n, m;
vector<int> graph[MAXN];

int visit[MAXN];
int in_stack[MAXN];
bool cycle;

void dfs(int node) {
    visit[node] = true;
    in_stack[node] = true;
    for (int child : graph[node]) {
        if (in_stack[child]) {
            cycle = true;
        } else if (!visit[child]) {
            dfs(child);
        }
    }

    in_stack[node] = false;
}

int main() {
    scanf("%d %d", &n, &m);
    int x, y;
    for (int i = 0; i < m; ++i) {
        scanf("%d %d", &x, &y);
        graph[x].push_back(y);
    }

    cycle = false;
    memset(visit, 0, sizeof(visit));
    for (int i = 1; i <= n; ++i) {
        if (!visit[i]) {
            dfs(i);
        }
    }

    printf("%s\n", cycle ? "YES" : "NO");

    return 0;
}
