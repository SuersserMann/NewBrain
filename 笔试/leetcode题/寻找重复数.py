class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict={}
        n=len(nums)
        for i in nums:
            if i not in dict:
                dict[i]=i
            else:
                return i

