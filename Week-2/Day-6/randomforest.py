from sklearn.ensemble import RandomForestRegressor

import numpy as np
#Regression
X=np.array([[1],[2],[3],[4]])
y=[1,4,9,16]

model=RandomForestRegressor(n_estimators=100,max_depth=5)

model.fit(X,y)

print(model.predict([[5]]))

#Classification

from sklearn.ensemble import RandomForestClassifier

# Data
X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

# Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Prediction
print(model.predict([[2.6]]))




