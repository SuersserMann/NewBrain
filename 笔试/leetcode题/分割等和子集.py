class Solution:
    def canPartition(self, nums):
        amount = sum(nums)
        if amount % 2 == 1:
            return False
        count = int(amount / 2)
        n = len(nums)
        dp = [[False] * (amount + 1) for _ in range(n + 1)]
        for row in range(n + 1):
            dp[row][0] = True
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][count]


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
