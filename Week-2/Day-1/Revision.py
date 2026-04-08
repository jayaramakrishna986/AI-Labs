import numpy as np
matr=np.array([[1,2],
      [4,2],
      [3,1]])
matr1=np.array([[2,3,4],
       [4,1,2],
       [1,3,1]])

# print(np.dot(matr,matr1))
# print(matr@matr1)

# e_values,e_vectors=np.linalg.eig(matr1)
# print(e_values)
# print(e_vectors)

# print(np.linalg.inv(matr1))
# print(np.linalg.det(matr1))
# print(np.linalg.matrix_rank(matr))

# print(np.linalg.norm(matr1,ord=1))

import pandas as pd

df=pd.read_csv("DataSets\StudentPerformanceFactors.csv")
# print(df.head())

# print(df["Hours_Studied"])
# print(max(df["Hours_Studied"]))

# print(df.describe())
print(df.fillna("as"))