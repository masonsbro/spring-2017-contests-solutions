#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int MOD = 1000000007;
const int MAXN = 1000006;
int dp[MAXN];

void sum(int& a, int b) {
    a += b;
    if (a >= MOD) {
        a -= MOD;
    }
}

void precompute() {
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;
    dp[1] = 2;
    int s = 3;

    for (int i = 2; i < MAXN; ++i) {
        sum(dp[i], dp[i - 2]);
        sum(dp[i], dp[i - 1]);
        sum(dp[i], s);

        sum(s, dp[i]);
    }
}

int main() {
    precompute();

    int T;
    scanf("%d", &T);

    int x;
    while (T-- > 0) {
        scanf("%d", &x);
        printf("%d\n", dp[x]);
    }
    return 0;
}

