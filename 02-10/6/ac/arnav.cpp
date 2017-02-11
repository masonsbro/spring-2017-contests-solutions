#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <cassert>

using namespace std;

const int MAXN = 110000;
const int NULL_NODE = 0;

int first;
int last;

int prev_node[MAXN];
int next_node[MAXN];

string names[MAXN];
map<string, int> inverse_names;
int next_id;

void sever_ties(int x) {
    int before = prev_node[x];
    int after = next_node[x];

    if (before != NULL_NODE) {
        next_node[before] = after;
    }

    if (after != NULL_NODE) {
        prev_node[after] = before;
    }

    if (first == x) {
        first = after;
    }

    if (last == x) {
        last = before;
    }

    prev_node[x] = NULL_NODE;
    next_node[x] = NULL_NODE;
}

void call_delete() {
    if (first == NULL_NODE) {
        cout << "NONE\n";

        return;
    }

    int cur = first;
    sever_ties(first);

    cout << names[cur] << '\n';
}

void create_node(const string name) {
    names[next_id] = name;

    prev_node[next_id] = NULL_NODE;
    next_node[next_id] = NULL_NODE;

    inverse_names[name] = next_id;

    ++next_id;
}

void move_to_front(const string name) {
    int id = inverse_names[name];

    sever_ties(id);

    if (first == NULL_NODE) {
        first = id;
        last = id;
    } else {
        prev_node[first] = id;
        next_node[id] = first;
        first = id;
    }
}

void print_list() {
    printf("-------------\n");
    int cur = first;
    while (cur != NULL_NODE) {
        printf("%x %x %s %x\n", cur, prev_node[cur], names[cur].c_str(), next_node[cur]);
        cur = next_node[cur];
    }
    printf("-------------\n");
}

int main() {
    int num_tests;
    cin >> num_tests;
    assert(1 <= num_tests and num_tests <= 10);

    int num_commands;
    string command, name;

    while (num_tests-- > 0) {
        memset(prev_node, 0, sizeof(prev_node));
        memset(next_node, 0, sizeof(next_node));
        first = NULL_NODE;
        last = NULL_NODE;
        inverse_names.clear();
        next_id = 1;

        cin >> num_commands;

        assert(0 <= num_commands and num_commands <= MAXN);

        while (num_commands-- > 0) {
            cin >> command;

            if (command == "DELETE") {
                call_delete();
            } else {
                cin >> name;
                if (inverse_names.find(name) == inverse_names.end()) {
                    create_node(name);
                }

                move_to_front(name);
            }

            // print_list();
        }

        if (num_tests > 0) {
            cout << '\n';
        }
    }

    return 0;
}
