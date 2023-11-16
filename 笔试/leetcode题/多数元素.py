class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        m = n / 2
        if n==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] = dict[nums[i]] + 1
                if dict[nums[i]] > m:
                    return nums[i]
            else:
                dict[nums[i]] = 1
