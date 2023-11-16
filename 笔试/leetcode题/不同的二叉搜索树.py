class Solution:
    def numTrees(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


s = Solution()
print(s.numTrees(3))
