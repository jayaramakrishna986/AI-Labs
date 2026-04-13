import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

a=np.array([1,2,3,4,5,6]).reshape(-1,1)
b=[0,0,0,1,1,1]

model=LogisticRegression()
model.fit(a,b)
y_pred=model.predict([[2]])
print(y_pred)
