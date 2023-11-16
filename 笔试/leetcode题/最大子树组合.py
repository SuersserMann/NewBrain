class Solution:
    def maxSubArray(self, nums):
        dp = [0 for _ in range(len(nums))]
        if not nums:
            dp[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= 0:
                dp[i] = max(nums[i], (dp[i-1] + nums[i]))
            else:
                dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
