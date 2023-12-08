import numpy as np

np.random.seed(0)
x_train = (np.random.rand(1000) * 2 - 1) * 100
y_train = x_train * 1.477 + 0.089

random_value = np.random.normal(0, 1, 1000)
# y_train = y_train + random_value
# print(y_train)
n = len(x_train)


# x_mean = np.mean(x_train)/100
# x_std = np.std(x_train)/100
# x_train = (x_train - x_mean) / x_std


def MSE(w, b, x, y, count):
    res = 0
    for i in range(count):
        y_pre = w * x[i] + b
        loss_error = (y_pre - y[i]) ** 2
        res += loss_error
    return res / count


#
# print(MSE(0, 0, x_train, y_train, 100))


def step_gradient(w, b, x, y, count, lr):
    w_gradient = 0
    b_gradient = 0
    for i in range(count):
        w_gradient += (2 / count) * x[i] * ((w * x[i] + b) - y[i])
        b_gradient += (2 / count) * ((w * x[i] + b) - y[i])
    return w - lr * w_gradient, b - lr * 1000 * b_gradient


#
# print(step_gradient(0, 0, x_train, y_train, 100, 0.01))


def step_loop(w, b, x, y, count, lr, step):
    w_cur = w
    b_cur = b
    for i in range(step):
        w_cur, b_cur = step_gradient(w_cur, b_cur, x, y, count, lr)
        # print(w_cur, b_cur)
    return w_cur, b_cur


print(MSE(2, 0, [1, 2, 3], [2, 4, 8], 3))
print(step_gradient(2, 0, [1, 2, 3], [2, 4, 8], 3, 0.01))
# print(step_loop(2, 0, [1, 2, 3], [2, 4, 7], 3, 0.01, 100))
print(step_loop(0, 0, x_train, y_train, 1000, 1e-5, 1000))
# 这里面需要注意，一个是初始化w,b很重要，第二，梯度下降的方式很重要，第三，学习率选择很重要，第四，迭代的次数很重要
