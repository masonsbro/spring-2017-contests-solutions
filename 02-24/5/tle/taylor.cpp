#include <iostream>

using namespace std;

long long MOD = 1000000007;

int main() {
   int num_tests;

   cin >> num_tests;
   cout << num_tests << " tests" << endl;

   for (int i = 0; i < num_tests; i++) {
      long long dp[1000000] = {0};
      long long num_stairs;
      cin >> num_stairs;
      cout << num_stairs << " stairs" << endl;

      dp[num_stairs] = 1;
      for (int j = num_stairs - 1; j >= 0; j--) {
         long long step = dp[j + 1]; /* A step from the previous stair. */

         long long double_step = 0;
         if (j + 2 <= num_stairs)
            double_step = dp[j + 2]; /* A step down from two steps prior. */

         long long slides = 0;
         for (int k = j + 1; k <= num_stairs; k++)
            slides += dp[k]; /* A slide from any prior step to here. */

         dp[j] = (step + double_step + slides) % MOD;

         cout << "dp[stair " << j << "] = " << dp[j] << endl;
      }
      cout << dp[0] << endl;
   }
}
