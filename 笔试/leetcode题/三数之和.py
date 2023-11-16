class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        else:
            nums.sort()

            res = []
            for i in range(1, len(nums) - 1):
                l = 0
                r = len(nums) - 1
                while l<i<r:
                    s = nums[l] + nums[i] + nums[r]
                    if s > 0:
                        r -= 1
                    elif s < 0:
                        l += 1
                    else:

                        if [nums[l], nums[i], nums[r]] not in res:
                            res.append([nums[l], nums[i], nums[r]])
                        l += 1
                        r -= 1
        return res


s = Solution()
print(s.threeSum(
    [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
