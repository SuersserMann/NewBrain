from math import sqrt
import torch
import torch.nn as nn


class SelfAttention(nn.Module):
    def __init__(self, input_dim, heads):
        super(SelfAttention, self, ).__init__()
        self.input_dim = input_dim
        self.heads = heads
        self.head_dim = self.input_dim // self.heads
        self.q = nn.Linear(input_dim, self.head_dim)
        self.k = nn.Linear(input_dim, self.head_dim)
        self.v = nn.Linear(input_dim, self.head_dim)
        self.fc = nn.Linear(input_dim, input_dim)

    def forward(self, query, key, value, mask):
        batch_size = query.shape[0]
        q_len, k_len, v_len = query.shape[1], key.shape[1], value.shape[1]
