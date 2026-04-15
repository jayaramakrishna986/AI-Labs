import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X=np.array([[1],[2],[3],[4]])

y=[1,4,9,16]



poly=PolynomialFeatures(degree=2)

X_poly=poly.fit_transform(X)

model=LinearRegression()
model.fit(X_poly,y)

print(model.predict(poly.transform([[5]])))
X_range = np.linspace(1, 5, 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_pred = model.predict(X_range_poly)
# plt.scatter(X,y,label="Original Data")
plt.scatter(X, y, label="Original Data")       
plt.plot(X_range, y_pred, label="Polynomial Curve") 
# plt.plot()
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()