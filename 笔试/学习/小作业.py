# a = 0
#
# for i in range(1, 101):
#     a += i ** 2
#
# print(a)

# a = 0
# for i in range(1, 1001):
#     if i % 3 == 0 or i % 5 == 0:
#         a += i
#         print(i)
#     else:
#         continue

# x = "supercalifragilisticexpialidocious"
# y = "pneumonoultramicroscopicsilicovolcanoconiosis"
# for i in x:
#     if i not in y:
#         print(i, end='')

# import random
# random_integers = [random.randint(1, 100) for _ in range(5)]
# with open('rand.txt', 'w') as file:
#     for num in random_integers:
#         file.write(str(num) + '\n')

# input_string = "antidisestablishmentarianism"
# sorted_string = ''.join(sorted(input_string))
# print(sorted_string)

# x, y = 0, 0
# route = 'NNNEEESSWNNSW'
# for i in route:
#     if i == 'N':
#         y += 1
#     elif i == 'S':
#         y -= 1
#     elif i == 'E':
#         x += 1
#     else:
#         x -= 1
# print(f'({x},{y})')

# import numpy as np
#
# x = np.random.randint(1, 11, 100)
# dict = {}
# for i in x:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] = dict[i] + 1
#
# for i in range(1, 11):
#     if i not in dict:
#         print(f'{i}.')
#     else:
#         print(f'{i}.', end='')
#         for j in range(dict[i]):
#             print('*', end='')
#         print()

# jsonlike = {12345: {"info": {"name": "Rudy",
#                              "course": {"ECMM445": {"grade": 0, "classification": "x", "marks": [50, 29]},
#                                         "ECMM443": {"grade": 0, "classification": "x", "marks": [10, 4]},
#                                         "ECM3441": {"grade": 0, "classification": "x", "marks": [40, 24]},
#                                         "ECM3433": {"grade": 0, "classification": "x", "marks": [24, 34]}, },
#                              "age": 103, }}}
#
# x = (jsonlike[12345])
# x_info = (x['info'])
# x_course = x_info['course']
#
# for i in x_course:
#     cur = x_course[i]
#     grade=sum(cur['marks'])
#     cur['grade'] = grade
#     if grade>=70:
#         cur['classification']='Distinction'
#     elif 60<grade<69:
#         cur['classification']='Merit'
#     elif 50<grade<59:
#         cur['classification'] = 'Pass'
#     elif 40<grade<49:
#         cur['classification'] = 'Condonable Fail'
#     else:
#         cur['classification']='Fail'
#
# print(jsonlike)

