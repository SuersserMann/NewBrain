import torch
import torch.nn as nn


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        assert d_model % num_heads == 0
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)

    def forward(self, input, mask=None):
        batch_size, seq_len, d_model = input.size()

        # Linearly transform input to obtain query, key, and value
        Q = self.W_q(input)
        K = self.W_k(input)
        V = self.W_v(input)

        # Split the heads for multi-head attention
        Q = Q.view(batch_size, -1, self.num_heads, self.head_dim)
        K = K.view(batch_size, -1, self.num_heads, self.head_dim)
        V = V.view(batch_size, -1, self.num_heads, self.head_dim)

        Q = Q.permute(0, 2, 1, 3)  # (batch_size, num_heads, seq_len, head_dim)
        K = K.permute(0, 2, 1, 3)
        V = V.permute(0, 2, 1, 3)

        # Calculate scaled dot-product attention scores
        scores = torch.matmul(Q, K.permute(0, 1, 3, 2)) / (self.head_dim ** 0.5)

        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)

        # Apply the softmax function to obtain attention weights
        attention_weights = torch.nn.functional.softmax(scores, dim=-1)

        # Compute the output of the attention mechanism
        out = torch.matmul(attention_weights, V)

        # Reshape and concatenate the heads
        out = out.permute(0, 2, 1, 3).contiguous().view(batch_size, -1, self.d_model)

        return out, attention_weights


