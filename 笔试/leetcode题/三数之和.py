class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        else:
            nums.sort()
            res = []
            for left in range(len(nums) - 1):
                # 去除掉left出现过的，如果往后算会去除掉没有使用的mid
                if left > 0 and nums[left] == nums[left - 1]:
                    continue
                mid = left + 1
                right = len(nums) - 1
                if nums[left] > 0:
                    break
                while mid < right:
                    cur = nums[left] + nums[mid] + nums[right]
                    if cur > 0:
                        right -= 1
                    elif cur < 0:
                        mid += 1
                    else:
                        res.append([nums[left], nums[mid], nums[right]])
                        mid += 1
                        right -= 1
                        while mid < right and nums[right] == nums[right + 1]: right -= 1
                        while mid < right and nums[left] == nums[left - 1]: left += 1
        return res


s = Solution()
print(s.threeSum(
    [-1, 0, 1, 2, -1, -4]))
