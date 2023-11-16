class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        dp = [1] * (n + 1)
        dp1 = [1] * (n + 1)
        res = []
        for i in range(n):
            dp[i + 1] = dp[i] * nums[i]
            dp1[n - i - 1] = dp1[n - i] * nums[n - 1 - i]
        for i in range(n):
            res.append(dp[i] * dp1[i + 1])
        return res


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
