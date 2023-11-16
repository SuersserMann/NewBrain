import math

import numpy as np
import matplotlib.pyplot as plt
# # ex1
# play_card = ['方块', '红桃', '黑桃', '梅花']
# a = int(np.random.choice(4, 1))
# print(play_card[a])
#
# # ex1-2
# # print(math.comb(6, 2))
# dice1 = int(np.random.choice(7, 1))
# dice2 = int(np.random.choice(7, 1))
# print(dice1 + dice2)
#
# # ex1-3
# coin = ['positive', 'negative']
#
#
# def roll(n):
#     res = []
#     for _ in range(n):
#         res.append(coin[int(np.random.choice(2, 1))])
#     return res
#
#
# print(roll(3))
#
# # ex2
# print(math.comb())


# ex1
def gaussian(x, mu, sigma):
    return np.exp(-(x - mu) ** 2 / (2 * (sigma ** 2))) / (sigma * math.sqrt(2 * math.pi))


x = np.arange(-3, 3, 0.1)
m = 0;
s = 1;
plt.plot(x, gaussian(x, m, s), label=r"$\mu$ = {}, $\sigma$ = {}".format(m, s))
m = 1;
s = 1;
plt.plot(x, gaussian(x, m, s), label=r"$\mu$ = {}, $\sigma$ = {}".format(m, s))
m = 0;
s = 2;
plt.plot(x, gaussian(x, m, s), label=r"$\mu$ = {}, $\sigma$ = {}".format(m, s))
m = -2;
s = 4;
plt.plot(x, gaussian(x, m, s), label=r"$\mu$ = {}, $\sigma$ = {}".format(m, s))
plt.legend()
plt.show();
