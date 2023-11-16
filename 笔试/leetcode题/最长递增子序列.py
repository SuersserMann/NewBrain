from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums) -> int:
        ng = 0  # g 的长度
        for x in nums:
            j = bisect_left(nums, x, 0, ng)
            nums[j] = x
            if j == ng:  # >=x 的 g[j] 不存在
                ng += 1
        return ng


nums = [0, 1, 0, 3, 2, 3]
s = Solution()
print(s.lengthOfLIS(nums))
