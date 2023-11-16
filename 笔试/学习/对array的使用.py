import numpy as np

# a = [1, 4.0, 6]
# print(a)
# print(type(a))
# b = np.array(a)
# print(b)
# print(type(b))
# c = b * 5 - 3
# print(c)
# print(type(c))
# print(b)
# d = b.tolist()
# print(d)
# print(type(d))

# def make_successor(step):
#     return lambda val: val + step
#
#
# print(make_successor(1))

# print(np.linspace(0, 10, 51))

# x = np.array([[[111, 112], [121, 122]],
#               [[211, 212], [221, 222]],
#               [[311, 312], [321, 322]]])
#
# print(x[0, 0, 0])#more efficient

# x = np.array([
#     [11, 12, 13, 14, 15],
#     [21, 22, 23, 24, 25],
#     [31, 32, 33, 34, 35],
#     [41, 42, 43, 44, 45],
#     [51, 52, 53, 54, 55]])
#
# print(x > 25)
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

features = iris.data.T
print(features)
plt.scatter(features[0], features[1], alpha=0.2, s=100 * features[3],
            c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
# plt.show()
