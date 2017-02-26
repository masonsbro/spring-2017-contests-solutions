#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 100005;
int c[MAXN];

int main() {
    int s, t;
    scanf("%d %d", &s, &t);

    long long sum = 0;
    for (int i = 0; i < s; ++i) {
        scanf("%d", &c[i]);
        c[i] = t / c[i];
        
        sum += c[i];
    }
    
    printf("%lld\n", sum);
    for (int i = 0; i < s; ++i) {
        printf("%d ", c[i]);
    }

    return 0;
}

