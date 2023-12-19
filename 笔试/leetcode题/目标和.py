class Solution:
    def findTargetSumWays(self, nums, target) -> int:
        all_s = sum(nums)

        if (all_s + target) % 2 != 0 or target > all_s or target < -all_s:
            return 0
        pos = (all_s + target) // 2
        dp = [0] * (pos + 1)
        dp[0] = 1
        for num in nums:
            for j in range(pos, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]
        return dp[-1]


solution = Solution()
nums = [1, 1, 1, 1, 1]
target = 3
result = solution.findTargetSumWays(nums, target)
print(result)
