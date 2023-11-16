import random

import numpy as np

a_list = np.random.randint(1, 101, 100)


def quicksort(nums, left, right):
    pivot = nums[random.randint(left, right)]
    i, j = left, right
    while i <= j:
        while nums[i] < pivot: i += 1
        while pivot < nums[j]: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    if i < right: quicksort(nums, i, right)
    if j > left: quicksort(nums, left, j)
    return nums


print(quicksort(a_list, 0, len(a_list) - 1))
