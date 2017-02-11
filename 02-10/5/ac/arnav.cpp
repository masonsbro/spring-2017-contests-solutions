#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int T;
    scanf("%d", &T);

    int num_points;
    int speed, duration;

    while (T-- > 0) {
        scanf("%d", &num_points);

        long long dist = 0;
        long long time = 0;
        for (int i = 0; i < num_points; ++i) {
            scanf("%d %d", &speed, &duration);
            dist += (1LL * speed * duration);
            time += duration;
        }

        long long ans = (dist + (time / 2LL)) / time;
        printf("%lld\n", ans);
    }

    return 0;
}
