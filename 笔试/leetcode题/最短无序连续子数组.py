class Solution:
    def findUnsortedSubarray(self, nums):
        left, right, min_num, max_num = 0, 0, float("inf"), float("-inf")

        for i, j in enumerate(nums):
            if j < max_num:
                right = i
            else:
                max_num = max(max_num, j)

            if nums[len(nums)-1-i] > min_num:
                left = len(nums)-1-i
            else:
                min_num = min(min_num, nums[len(nums)-1-i])
        return 0 if left == right else right - left + 1


s = Solution()
print(s.findUnsortedSubarray([4, 5, 6, 0, 7, 8, 9]))
