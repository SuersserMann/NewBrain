# 二分查找必须在有序数组之内
a_list = list(range(1, 21))
print(a_list)
b = 18


# 返回其index，无则返回-1
def find(b, a_list):
    if not a_list:
        return -1
    else:
        l = 0
        r = len(a_list) - 1

        while l <= r:
            p = (l + r) // 2
            if a_list[p] > b:
                r = p - 1
            elif a_list[p] < b:
                l = p + 1
            else:
                return p


print(find(b, a_list))
