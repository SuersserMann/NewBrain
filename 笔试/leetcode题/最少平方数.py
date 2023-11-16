class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = min(dp[i - j ** 2]+1 for j in range(1, int(i ** 0.5) + 1))
        return dp[-1]


s = Solution()
print(s.numSquares(12))
