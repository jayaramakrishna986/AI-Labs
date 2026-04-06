# # The NumPy array is a data structure that efficiently stores and accesses multidimensional 
# # arrays (also known as tensors), and enables a wide variety of scientific computation. 
# # It consists of a pointer to memory, along with metadata used to interpret the data stored there, notably ‘data type’, ‘shape’ and ‘strides ###

import numpy as np

arr=np.array([1,6,65,98,21])

print(arr)

print(arr+2)
print(arr*2)
print(np.zeros(10))
print(np.ones(6))
# 2D Visuvalization
arr1=np.array([
    [1,2,3],
    [6,7,8],
    [4,5,7]
])
print(arr1)

print("0th row 2nd index",arr1[0,2])

print(arr1.ndim)#To view the Array Dimensions
print(arr1.shape)#It tell does the numof rows to cloums in the array

print(arr1.size)# number of elements in the given array

print(arr1.dtype)

print(arr1.nbytes)#number of elements x size of data type(9*8=72)


print(arr1.itemsize)#size of each element in the array

print(arr1.T)#Transpose of a Matrix

print(np.arange(0,10,1))# same as the Slicing 

print(np.linspace(10,30,5))
arr3=np.arange(6)
print(arr3.reshape(3,2))


arr4=np.array([1,2,3])

print(np.mean(arr4))
print(np.min(arr4))
print(np.sum(arr4))
print(np.std(arr4))
print(arr4[arr4>2])

# print(np.random.rand(100))

arr6=np.array([1,3,6,9,67,78])

print(np.reshape(2,-1))

print(np.random.randint(1,10,5))
print(np.random.rand(3))
