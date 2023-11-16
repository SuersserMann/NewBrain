class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)
        while i<j:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
        return nums
