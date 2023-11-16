class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        else:
            l = 0
            r = len(nums) - 1
            if target >= nums[0]:
                left = True
            else:
                left = False
            while l <= r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    return mid
                if left:
                    if nums[mid] < nums[0]:
                        r = mid - 1
                    else:
                        if nums[mid]>target:
                            r=mid -1
                        else:
                            l=mid+1
                else:
                    if nums[mid] > nums[-1]:
                        l = mid + 1
                    else:
                        if nums[mid]<target:
                            l = mid+1
                        else:
                            r= mid -1


        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
