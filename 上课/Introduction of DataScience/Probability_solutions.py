import scipy.special
import matplotlib.pyplot as plt
import math
import numpy as np

# Exercise 1
# P( dice1 = 6 | dice2 = 6) = P(dice1 = 6 and dice2 = 6) / P(dice1 = 6) = (1/36)/(1/6) = 1/6
# P( dice1 = 6 | dice2 = 6) = P( dice1 = 6 ) = 1/6

# Exercise 2
#  P( dice1 = 4 or dice2 = 4 | dice1 + dice2 = 7) = P( (dice1 = 4 or dice2 = 4) and (dice1 + dice2 = 7) )/P(dice1 + dice2 = 7)
# = P( (dice1 = 4 or dice2 = 4) and (dice1 + dice2 = 7) )/ (1/6)
# = (2/36) * 6 = 1/3

# Alternatively count in the
# reduced sample space where sum is 7: {(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)}
# Just by counting: 2/6 = 1/3

# Exercise 3
# P(5) = (10 choose 5) p^5 (1-p)^5 
import scipy.special

print(scipy.special.binom(10, 5) * (0.5) ** 5 * (0.5) ** 5)


# Exercise 4
def binomial(n, p):
    return [scipy.special.binom(n, k) * p ** k * (1 - p) ** (n - k) for k in
            range(n + 1)]  ##For small n this will work okay, but potential to have big rounding error!]


n = 10;
p = 0.5;
plt.scatter(range(n + 1), binomial(n, p), label="n={}, p={}".format(n, p), color='b');
plt.plot(range(n + 1), binomial(n, p), color='b')
n = 20;
p = 0.5;
plt.scatter(range(n + 1), binomial(n, p), label="n={}, p={}".format(n, p), color='orange');
plt.plot(range(n + 1), binomial(n, p), color='orange')
n = 10;
p = 0.1;
plt.scatter(range(n + 1), binomial(n, p), label="n={}, p={}".format(n, p), color='m');
plt.plot(range(n + 1), binomial(n, p), color='m')
plt.legend()
plt.xlabel("k")
plt.ylabel("P(k)")
# plt.show()
plt.close()


# Exercise 5
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
# plt.show();
plt.close();


# Exercise 6
def flip_coin():
    if np.random.rand() < 0.5:
        return 0;
    return 1;


x = [];
m = [];
for N in range(10, 1000, 10):
    data = [flip_coin() for i in range(N)]
    x.append(N);
    m.append(np.mean(data));

plt.scatter(x, m)
# plt.show()
plt.close();

# Exercise 7
start = 10
count = 0;
stake = []
while start > 0:
    res = flip_coin();
    if res == 0:
        start -= 1
    else:
        start += 1
    stake.append(start)
    count += 1
plt.plot(range(count), stake)
# plt.show()

# Exercise 8
for N in [10, 100, 1000]:
    data = []
    for it in range(1000):
        experiment = [flip_coin() for i in range(N)]
        data.append(np.mean(experiment));
    plt.hist(data, bins=20, alpha=0.5, label="N = {}".format(N));
plt.legend();
# plt.show();
plt.close();

# Exercise 9
y = gaussian(np.arange(-5, 5, 0.01), 0, 1)
tot_sum = np.sum(y)
py = gaussian(np.arange(-1, 1, 0.01), 0, 1)
p_sum = np.sum(py)
print("+/- 1 std_dev ~ ", p_sum / tot_sum)

# Exercise 10
sdata = []
for N in range(10, 1000, 10):
    data = []
    for it in range(100):
        experiment = [flip_coin() for i in range(N)]
        data.append(np.mean(experiment));
    sdata.append(np.std(data))

x = np.log(range(10, 1000, 10))
plt.scatter(np.log(range(10, 1000, 10)), np.log(sdata))
plt.plot(x, -0.5 * x)
plt.legend();
# plt.show();
plt.close();

# Exercise 11
data = np.random.rand(10000)
plt.hist(data, bins=20, density=True, alpha=0.5)
# plt.show();
plt.close();

# Exercise 12
data = np.random.rand(10000) + np.random.rand(10000)
plt.hist(data, bins=20, density=True, alpha=0.5)
# plt.show();
plt.close();

for n in range(3, 6):
    data = np.random.rand(10000)
    for k in range(n - 1): data += np.random.rand(10000)

    plt.hist(data, bins=50, density=True, alpha=0.5)
    plt.show();
    plt.close();
# It starts to look Gaussian very quickly!
# This is the Central limit theorem, the sum/average of N variables
# sampled from any distribution will be normally distributed for large
# enough N.
