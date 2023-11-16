import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = np.random.uniform(-100, 100, size=(100, 1))
y = x ** 3 + 2 * x ** 2 + 2 * x + 100 * np.random.uniform(-100, 100, size=(100, 1))

poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

model = linear_model.Ridge(alpha=1)
model.fit(x_poly, y)

X_test = np.linspace(-100, 100, 100).reshape(-1, 1)
X_test_poly = poly.transform(X_test)
y_pred = model.predict(X_test_poly)

# 可视化结果
plt.scatter(x, y, label='Training Data')
plt.plot(X_test, y_pred, color='r', label='Polynomial Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
