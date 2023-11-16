# 每次找到列表中最大的放在最后面，然后两两比较，大则交换位置
import numpy as np

a_list = np.random.randint(1, 101, 100)
for i in range(len(a_list) - 1):
    for j in range(len(a_list) - 1 - i):
        if a_list[j] > a_list[j + 1]:
            a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

print(a_list)