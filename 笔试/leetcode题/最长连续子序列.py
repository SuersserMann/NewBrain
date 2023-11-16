class Solution:
    def longestConsecutive(self, nums) -> int:
        nums=list(set(nums))
        if not nums:
            return 0
        nums = sorted(nums)
        res = 1
        cur = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - 1 == nums[i]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        return res