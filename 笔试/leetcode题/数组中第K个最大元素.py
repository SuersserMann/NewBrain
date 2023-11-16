import random

class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)

        def quicksort(l, r):
            pivot = nums[random.randint(l, r)]
            i, j = l, r
            while i < j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            if i < r:
                quicksort(i, r)
            if j > l:
                quicksort(l, j)

        quicksort(0, n - 1)
        return nums[n - k]

s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))
