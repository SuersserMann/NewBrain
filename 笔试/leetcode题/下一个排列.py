class Solution:
    def nextPermutation(self, nums):
        a=sorted(nums)
        if nums==a[::-1]:
            nums[:]=a
            return
        i = len(nums) - 2
        j = len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        z = len(nums) - 1
        while z >= 0 and nums[z] <= nums[i]:
            z -= 1
        nums[i], nums[z] = nums[z], nums[i]
        nums[:] = nums[:j] + nums[j:][::-1]


nums = [1,1,5]
s = Solution()
s.nextPermutation(nums)
print(nums)
