# import matplotlib.pyplot as plt

# a=[1,2,3,8,5]
# b=[2,4,6,10008,10]

# plt.scatter(a,b)
# plt.show()


# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# data={
#     "experience":[1,2,3,4,5],
#     "salary":[30000,40000,50000,60000,70000]
# }
# df=pd.DataFrame(data)

# x=df[["experience"]]
# y=df[["salary"]]

# model=LinearRegression()

# model.fit(x,y)
# predicted_salary=model.predict([[6]])
# print(predicted_salary)
# plt.scatter(x,y)
# # plt.show()
# plt.plot(x,model.predict(x))
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()


# data={
#     "age":[1,2,3,4,5],
#     "Salary":[10000,20000,30000,40000,50000]
# }
# df=pd.DataFrame(data)
# print(df)

# x=df[["age"]]
# y=df[["Salary"]]

# model=LinearRegression()
# model.fit(x,y)

# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt


# data={
#     "Age":[10,56,25,2,52,56],
#     "Names":[10,20,20,20,20,2]    
#     }

# df=pd.DataFrame(data)
# # print(df)

# x=df[["Age"]]
# y=df[["Names"]]

# model=LinearRegression()
# model.fit(x,y)

# predicted=model.predict([[4]])
# print(predicted)

# plt.scatter(x,y)
# plt.plot(x,model.predict(x))
# plt.xlabel("Age")
# plt.ylabel("Names")
# plt.title("Linear regression")
# plt.show()
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy as stats
data={
    "Age":[10,12,23,14,15],
    "Salary":[10000,20000,30000,20000,12000]
}

df=pd.DataFrame(data)


x=df[["Age"]]
y=df[["Salary"]]
model=LinearRegression()
model.fit(x,y)

predictted=model.predict([[5]])

print(predictted)

plt.scatter(x,y)
plt.plot(x, model.predict(x), color='black')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age Vs Salary")
plt.show()

slope,intercept,r,p,std_err=stats.linregress(x,y)
print(slope,intercept,r,p,std_err)