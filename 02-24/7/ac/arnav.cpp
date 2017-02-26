#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>

using namespace std;
map<int, vector<pair<int, int> > > ans;

struct Node {
    const int val;
    const int column;

    Node* left;
    Node* right;

    Node(const int val, const int column): val(val), column(column), left(nullptr), right(nullptr) {}
    ~Node() {
        delete left;
        delete right;
    }

    int insert(int new_val, int column = 0) {
        if (new_val < val) {
            if (left == nullptr) {
                left = new Node(new_val, column - 1);
                return column - 1;
            } else {
                return left->insert(new_val, column - 1);
            }
        } else {
            if (right == nullptr) {
                right = new Node(new_val, column + 1);
                return column + 1;
            } else {
                return right->insert(new_val, column + 1);
            }
        }
    }

    void traverse(int depth = 0) {
        if (left != nullptr) {
            left->traverse(depth + 1);
        }

        ans[column].push_back(make_pair(depth, val));

        if (right != nullptr) {
            right->traverse(depth + 1);
        }
    }
};

int main() {
    int T;
    scanf("%d", &T);

    int n;
    while (T-- > 0) {
        scanf("%d", &n);
        int x;
        scanf("%d", &x);

        Node* root = new Node(x, 0);

        for (int i = 1; i < n; ++i) {
            scanf("%d", &x);
            root->insert(x);
        }

        ans.clear();

        root->traverse();

        for (auto it = ans.begin(); it != ans.end(); ++it) {
            sort(ans[it->first].begin(), ans[it->first].end());
            for (auto x : ans[it->first]) {
                printf("%d ", x.second);
            }
        }
        puts("");

        delete root;
    }

    return 0;
}
