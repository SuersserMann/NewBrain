from sklearn.linear_model import LinearRegression
import numpy as np

Lr = LinearRegression()
x_train = np.random.rand(100).reshape(-1, 1)
y_train = 2 * x_train + 0.1
x_test = x_train + 0.1
Lr = Lr.fit(x_train, y_train)
res = Lr.predict(x_test)
coefficients = Lr.coef_
intercept = Lr.intercept_

# 打印参数
print("模型权重（系数）:", coefficients)
print("模型偏差（截距）:", intercept)
print(res)
