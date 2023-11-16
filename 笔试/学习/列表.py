import numpy as np

random_array = np.random.randint(0, 10, size=(3, 1))
x = np.reshape(random_array, (3,))
b = random_array.T
print(random_array)
print(x)
print(b)
str_array = np.array(["apple", "banana", "cherry", "date"])

# 打印NumPy数组
print(str_array)