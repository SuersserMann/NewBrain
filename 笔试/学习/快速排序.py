import random

import numpy as np

a_list = [1, 2, 2, 2, 2, 0, 0, 0, 1, 1]
print()


def quicksort(nums, left, right):
    flag = nums[random.randint(left, right)]  # 随机初始化哨兵位置
    i, j = left, right  # 设定从左到右的指针i，从右到左的指针j
    while i <= j:
        while nums[i] < flag: i += 1  # i从左往右扫，找到大于等于flag的数。
        while nums[j] > flag: j -= 1  # j从右往左扫，找到小于等于flag的数。
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]  # 交换左右指针下标对应的数值
            i += 1  # 左指针继续往右走
            j -= 1  # 右指针继续往左走
    if i < right: quicksort(nums, i, right)  # 递归解决flag左边的低位数组的排序
    if j > left:  quicksort(nums, left, j)  # 递归解决flag右边的低位数组的排序
    return nums


print(quicksort(a_list, 0, len(a_list) - 1))
