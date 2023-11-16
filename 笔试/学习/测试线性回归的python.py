from sklearn.linear_model import LinearRegression
import numpy as np
LR=LinearRegression()
x=np.random.randint(1,101,(10,1))
y=2*x
x_test=x*3
LR=LR.fit(x,y)
predict=LR.predict(x_test)
print(x)
print(y)
print(x_test)
print(predict)
