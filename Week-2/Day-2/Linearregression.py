# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np


# df = pd.read_csv(r"C:\Programs12\AI_Labs\AI-Labs\DataSets\StudentPerformanceFactors.csv")

# X=df[["Hours_Studied"]]
# y=df[["Exam_Score"]]
# # print(x,y)
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

# lr=LinearRegression()

# lr.fit(X_train,y_train)
# lr.predict(X_test([23]))
# print(X_test)
# plt.scatter(x,y)
# plt.xlabel("Hours Studied")
# plt.ylabel("Exam Score")
# # plt.plot(x,y)
# plt.show()

# import numpy as np
# import pandas as pd  
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# X=np.array([[1], [2], [3], [4], [5]])
# y = np.array([2, 4, 5, 4, 5])  
# model=LinearRegression()
# model.fit(X,y)

# y_pred=model.predict(X)

# print("Slope :",model.coef_)
# print("Intercept",model.intercept_)

# plt.scatter(X,y,color="blue")
# plt.plot(X,y_pred,color="red")
# plt.show()

# real world problem

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# X = [[1], [2], [3], [4], [5], [6]]
# y = [30000, 35000, 40000, 45000, 50000, 55000]

# model=LinearRegression()
# model.fit(X,y)

# y_pred=model.predict(X)

# plt.scatter(X,y,color="Yellow")
# plt.plot(X,y_pred,color="red")
# plt.show()
# print(model.predict([[7]]))


X = [[500], [800], [1000], [1200], [1500], [1800]]   # Size in sq ft
y = [150000, 200000, 250000, 300000, 350000, 400000]  # Price

model=LinearRegression()

model.fit(X,y)

y_pred=model.predict(X)

plt.scatter(X,y,color="Red")
plt.plot(X,y_pred,color="blue")
# plt.show()

print(model.predict([[2000]]))
print(model.predict([[750], [1600]]))