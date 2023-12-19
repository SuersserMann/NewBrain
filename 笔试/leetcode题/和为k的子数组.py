class Solution:
    def subarraySum(self, nums, k: int) -> int:
        res = 0
        pre = {0: 1}
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum - k in pre:
                res += pre[pre_sum - k]
            pre[pre_sum] = pre.get(pre_sum, 0) + 1
        return res


solution = Solution()
nums = [1, 2, 3]
k = 2
result = solution.subarraySum(nums, k)
print(result)
