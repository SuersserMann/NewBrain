import random


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        def quicksort(path, left, right):
            n = random.randint(left,right)
            pivot = path[n]
            l, r = left, right
            while l <= r:
                while path[l] < pivot:
                    l += 1
                while path[r] > pivot:
                    r -= 1
                if l <= r:
                    path[l], path[r] = path[r], path[l]
                    l += 1
                    r -= 1
            if l < right:
                quicksort(path, l, right)
            if r > left:
                quicksort(path, left, r)

        quicksort(nums, 0, len(nums) - 1)
        return nums


s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))
