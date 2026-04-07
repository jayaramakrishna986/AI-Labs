# from abc import abstractmethod,ABC
# class Student:
#     def __init__(self,data,name):
#         self.name=name
#         self.data=data

#     def Display(self):
#         print(f"name is {self.name} and data is {self.data}")

# class Attendence(ABC):
#     @abstractmethod
#     def calculate(self,present):
#         pass


# class t1(Attendence):
#     def calculate(self, present):
#         print(f"I am Present {present+1}")


# s1=Student("Data1","Jairam")
# s1.Display()
# t=t1()
# t.calculate(1)


import numpy as np
import pandas as pd
# arr1=np.array([[1,2,5],
#               [3,5,6]])
# print(arr1.T)

# print(np.linspace(1,10,5))

# print(np.arange(6))

# print(arr1.reshape(3,2))

# arr2=pd.Series([1,2,6,4],index=[1,2,3,4],name="Jello",dtype=float)

# print(max(arr2))

# arr3=pd.DataFrame({"id":[1,2,3,4,5]})
# print(arr3)

# # df=pd.read_csv("DataSets\StudentPerformanceFactors.csv",index=[1:3])

# df.head()


arre=np.array([[ 0,  5, 10, 15],
                [ 1,  6, 11, 16],
                [ 2,  7, 12, 17],
                [ 3,  8, 13, 18],
                [ 4,  9, 14, 19]])

print(arre.ravel())
print(arre.flatten())
print(arre.transpose()==arre.T)


ar1=np.array([[1,2],
              [3,5]])

ar2=np.array([[1,2],
              [2,3]])

print(np.cross(ar1,ar2))