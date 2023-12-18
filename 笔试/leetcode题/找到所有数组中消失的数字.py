class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        s = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            s[nums[i]] += 1
        for i in range(len(s)):
            if s[i] == 0:
                res.append(i)
        return res[1:]
