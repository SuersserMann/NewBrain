class Solution:
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                mid_l, mid_r = mid - 1, mid + 1
                res.append(mid)
                while mid_l >= 0 and nums[mid_l] == target:
                    res.append(mid_l)
                    mid_l -= 1
                while len(nums) - 1 >= mid_r and nums[mid_r] == target:
                    res.append(mid_r)
                    mid_r += 1
                return [min(res), max(res)]
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, -1]


s = Solution()
print(s.searchRange([1, 1, 2], 1))
