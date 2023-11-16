class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = amount
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return dp[-1] if dp[-1]!=float('inf') else -1