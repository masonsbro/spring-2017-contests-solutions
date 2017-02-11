#include <bits/stdc++.h>

using namespace std;

#define MAX_ll 1000000000000000007

ofstream tests("contest.in");

typedef long long ll;

void trickyCase1() {
  ll numNodes = 446;
  tests << 446 << " " << 99235 << endl;
  for(ll i = 1; i < numNodes; i++ ) {
    for(ll j = i + 1; j <= numNodes; j++ ) {
      tests << i << " " << j << endl;
    }
  }
}

void trickyCase2() {
  tests << 2 << " " << 1 << endl;
  tests << 1 << " " << 2 << endl;
}

void trickyCase3() {
  ll numNodes = 2 * 50000;
  ll numEdges = numNodes - 1;
  tests << numNodes << " " << numEdges << endl;
  for(ll i = 1; i < numNodes; i++ ) {
    tests << i << " " << i + 1 << endl;
  } 
}

void trickyCase4() {
  tests << 5 << " " << 6 << endl;
  tests << 1 << " " << 3 << endl;
  tests << 1 << " " << 2 << endl;
  tests << 3 << " " << 4 << endl;
  tests << 2 << " " << 4 << endl;
  tests << 3 << " " << 5 << endl;
  tests << 4 << " " << 5 << endl;
}

void generateRandomCase() {
  // use the weights trick but for each place where you can get "stuck", draw an edge from there to N
  ll N = rand() % 10000 + 20000;
  vector<ll> weights(N + 1);
  weights[1] = MAX_ll;
  weights[N] = 0;
  for(ll i = 2; i < N; i++ ) {
    ll t = 1000 * N;
    weights[i] = rand() % t;
  }
  unordered_map<ll, unordered_set<ll> > myGraph;
  unordered_set<ll> notIncluded;
  for(ll i = 2; i <= N; i++ ) {
    notIncluded.insert(i);
  }
  for(ll origin = 1; origin < N; origin++ ) {
    ll destination = 0;
    do {
      destination = rand() % (N + 1);
    } while(destination <= 1 || weights[destination] >= weights[origin] || destination == origin);
    myGraph[origin].insert(destination);
    notIncluded.erase(destination);
  }
  for(ll toDraw : notIncluded) {
    myGraph[1].insert(toDraw);
  }
  unordered_set<ll> holes;
  stack<ll> toVisit;
  unordered_set<ll> visited;
  toVisit.push(1);
  while(!toVisit.empty()) {
    ll c = toVisit.top();
    toVisit.pop();
    visited.insert(c);
    ll inserted = 0;
    for(ll neighbor : myGraph[c]) {
      if(visited.find(neighbor) == visited.end()) {
        toVisit.push(neighbor);
        inserted = 1;
      }
    }
    if(!inserted) {
      holes.insert(c);
    }
  }
  for(ll h : holes) {
    myGraph[h].insert(N);
  }
  for(ll i = 2; i < N; i++ ) {
    if(visited.find(i) == visited.end()) {
      myGraph[1].insert(i);
    }
  }
  ll numEdges = 0;
  for(auto &x : myGraph) {
    numEdges += x.second.size();
  }
  tests << N << " " << numEdges << endl;
  for(auto &x : myGraph) {
    for(ll y : x.second) {
      tests << x.first << " " << y << endl;
    }
  }
}

int main() {
  tests << 10 << endl;
  trickyCase1();
  trickyCase2();
  trickyCase3();
  trickyCase4();
  // for(ll i = 5; i <= 10; i++ ) {
  //   generateRandomCase();
  // }
  tests.close();
  return 0;
}