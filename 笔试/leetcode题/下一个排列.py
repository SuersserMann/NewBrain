# 先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
# 再找出另一个最大索引 l 满足 nums[l] > nums[k]；
# 交换 nums[l] 和 nums[k]；
# 最后翻转 nums[k+1:]。
# 举个例子：
#
# 比如 nums = [1,2,7,4,3,1]，下一个排列是什么？
#
# 我们找到第一个最大索引是 nums[1] = 2
#
# 再找到第二个最大索引是 nums[4] = 3
#
# 交换，nums = [1,3,7,4,2,1];
#
# 翻转，nums = [1,3,1,2,4,7]
#
# 完毕!

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
