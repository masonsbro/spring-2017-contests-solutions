#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int main() {
    int T;
    cin >> T;

    int n, m;
    string s;

    set<string> priority;
    vector<string> top, bottom;

    while (T-- > 0) {
        cin >> n;

        priority.clear();
        for (int i = 0; i < n; ++i) {
            cin >> s;
            priority.insert(s);
        }

        top.clear();
        bottom.clear();
        cin >> m;
        for (int i = 0; i < m; ++i) {
            cin >> s;
            if (priority.find(s) != priority.end()) {
                top.push_back(s);
            } else {
                bottom.push_back(s);
            }
        }

        sort(top.begin(), top.end());
        sort(bottom.begin(), bottom.end());

        for (auto s : top) {
            cout << s << '\n';
        }
        for (auto s : bottom) {
            cout << s << '\n';
        }
    }

    return 0;
}
