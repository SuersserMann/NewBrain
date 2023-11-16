import numpy as np
import pandas as pd
import torch
import matplotlib as plt
import torch.optim as optim
import warnings

warnings.filterwarnings('ignore')

from torch import nn


class MnistNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden1 = nn.Linear(784, 128)
        self.hidden2 = nn.Linear(128, 64)
        self.out = nn.Linear(64, 10)

    def forward(self, x):
        x = nn.relu(self.hidden1(x))
        x = nn.relu(self.hidden2(x))
        x = self.out(x)
        return x


net = MnistNet()
print(net)

for name, parameter in net.named_parameters():
    print(name, parameter, parameter.size())
