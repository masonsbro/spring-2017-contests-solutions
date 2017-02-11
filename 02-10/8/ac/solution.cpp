#include <bits/stdc++.h>

using namespace std;

int T;

int N, M;

vector<int> graph[100005];

typedef double ans_t;

vector<ans_t> answers; // number of legs
vector<int> visited;

ans_t solve(int start) {
  if(visited[start]) {
    return answers[start];
  }
  if(answers[start] != -1) {
    return answers[start];
  }
  if(start == N) {
    visited[N] = 1;
    answers[start] = 0;
    return 0;
  }
  visited[start] = 1;
  answers[start] = 0;
  for(int neighbor : graph[start]) {
    answers[start] += (1 + solve(neighbor));
  }
  answers[start] /= (graph[start].size());
  return answers[start];
}

void dumpAnswers() {
  for(int i = 1; i <= N; i++ ) {
    printf("answers[%d] = %f\n", i, answers[i]);
  }
}

int main() {
  scanf("%d\n", &T);
  vector<ans_t> toPrint(10);
  for(int h = 0; h < T; h++ ) {
    scanf("%d %d\n", &N, &M);
    answers.resize(N + 1);
    // graph.resize(N + 1);
    for(int i = 0; i < N; i++ ) {
      graph[i].clear();
    }
    visited.resize(N + 1);
    for(int i = 1; i <= N; i++ ) {
      answers[i] = -1;
    }
    for(int i = 0; i < M; i++ ) {
      int u, v;
      cin >> u >> v;
      graph[u].push_back(v);
    }
    toPrint[h] = solve(1);
    printf("%0.3lf\n", toPrint[h]);
    answers.clear();
    visited.clear();
  }
  // for(int h = 0; h < T; h++ ) {
  //   printf("%d\n", (int)(toPrint[h] + 0.5));
  // }
  return 0;
}
