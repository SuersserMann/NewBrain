from itertools import permutations

def get_permutations(nums):
    # 使用itertools库的permutations函数生成所有排列
    permutations_list = permutations(nums)

    # 将每个排列转换为整数并添加到结果集中
    result = []
    for p in permutations_list:
        num_str = ''.join(map(str, p))
        result.append(int(num_str))

    return result


# 示例输入
nums = [1, 2, 3]
result = get_permutations(nums)
print(result)
print()