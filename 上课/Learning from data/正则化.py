from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

ridge_regression = linear_model.Ridge(alpha=1.0)
x_train = np.random.rand(100).reshape(-1, 1)
y_train = x_train * 3
x_test = x_train+1
ridge_regression.fit(x_train, y_train)
lasso_regression = linear_model.Lasso(alpha=0.1)
lasso_regression.fit(x_train, y_train)
y_true = x_test * 3
y_l1 = lasso_regression.predict(x_test)
y_l2 = ridge_regression.predict(x_test)

# 绘制数据点
plt.scatter(x_train, y_train, label='Training Data', color='b')
plt.scatter(x_test, y_true, label='Test Data', color='g')

# 绘制 Ridge 回归线
plt.plot(x_test, y_l2, label='Ridge Regression', color='r')

# 绘制 Lasso 回归线
plt.plot(x_test, y_l1, label='Lasso Regression', color='m')

# 设置标题和标签
plt.title('Ridge and Lasso Regression')
plt.xlabel('X')
plt.ylabel('Y')

# 添加图例
plt.legend()

# 显示图形
plt.show()
