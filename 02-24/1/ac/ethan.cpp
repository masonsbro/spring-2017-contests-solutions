#include <cstdio>
#include <cassert>

using namespace std;

int t, c, g;

int main() {
    scanf(" %d", &t);
    assert(1 <= t && t <= 100);
    for (int q = 0; q < t; q++) {
        scanf(" %d %d", &c, &g);
        assert(c != g);
        assert(1 <= c && c <= 1000);
        assert(1 <= g && g <= 1000);
        if (c < g) printf("RIGHT\n");
        else printf("LEFT\n");
    }

    return 0;
}
