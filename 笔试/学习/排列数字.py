from itertools import permutations

nums = [1, 1, 0]
permutations_list = permutations(nums)
for i in permutations_list:
    print(list(i))

