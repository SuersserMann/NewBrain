import torch
from torch import tensor

x = tensor(42)
# print(x)
# print(x / 3)
# print(x.dim())
# print(x.item())

v = tensor([1.5, -0.5, 3.0])
# print(v.size())
# print(v.dim())

m = tensor([[1.5, -1], [2, -3]])
print(m)
print(m.size())
print(m.matmul(m))
print(m * m)

print(tensor([1., 2.]).matmul(m))
