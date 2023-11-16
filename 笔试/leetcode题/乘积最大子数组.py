class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        res = nums[0]
        min_a = nums[0]
        max_a = nums[0]

        for i in range(1, n):
            pre_min = min(nums[i], nums[i] * min_a, nums[i] * max_a)
            pre_max = max(nums[i], nums[i] * min_a, nums[i] * max_a)
            min_a = pre_min
            max_a = pre_max

            res = max(res, max_a)

        return res


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
