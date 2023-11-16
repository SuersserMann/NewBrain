import numpy as np
import torch
from matplotlib import pyplot as plt
import os
import warnings
warnings.filterwarnings("ignore")
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
x = torch.randint(0, 10, size=(10,))
out = torch.zeros(x.size(0), 10)
y = torch.LongTensor(x).view(-1, 1)
z = out.scatter_(dim=1, index=y, value=1)
# print(x)
# print(y)
# print(z)

cc = torch.randint(0, 256, size=(1, 28, 28))
plt.imshow(cc[0], cmap='gray', interpolation='none')
plt.xticks([])
plt.yticks([])
plt.show()

cc = torch.randint(0, 256, size=(3, 28, 28))  # 3表示3个通道，每个通道是28x28
cc = cc.byte()
cc = cc.permute(1, 2, 0)
plt.imshow(cc, interpolation='none')
plt.xticks([])
plt.yticks([])
plt.show()
