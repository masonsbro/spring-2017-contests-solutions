#include <cstdio>

using namespace std;

int t, a, b, c, n;

int main() {
    scanf(" %d", &t);
    for (int q = 0; q < t; q++) {
        scanf(" %d %d %d %d", &a, &b, &c, &n);
        long long ans = 0;
        for (int i = 1; i <= n; i++) {
            ans += i;
        }
        printf("%lld\n", 1L * a * b * c * ans);
    }

    return 0;
}
