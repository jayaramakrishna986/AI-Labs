import numpy as np

# ar1=np.array([1,3,4])



# v2=[1,3,5]
# v1=[56,8,7]

# r1=[v1[i]+v2[i] for i in range(len(v1))]
# print(r1)

# r2=sum([v1[i]*v2[i] for i in range(len(v1))])
# print(r2)

# f=[[1,244,4],
#    [3,4,56]]

# print(f[0][1])

# print(np.cross(v1,v2))
# print(np.dot(v1,v2))

# a1=[2,1]
# a2=[7,3]
# a3=np.dot(a1,a2)

# dot=sum(a1[i]*a2[i] for i in range(len(a1)))
# print(dot==a3)
# print(a1+a2)

# d1=np.array([1,2,3])
# d2=np.array([2,5,7])
# d3=sum(d1[i]*d2[i] for i in range(len(d1)))


# # Matrix Multiplication

# A=[[1,2],[3,4]]
# B=[[5,6],[7,8]]
# # res=[
# #     [
# #         sum(A[i][k]*B[k][j] for  k in range(2))
# #         for j in range(2)

# #     ]
# #     for i in range(2)
# #     ]
# # print(res)

# m1=[[1,2],[3,5]]
# m2=[[1,2],[1,2]]

# res=[
#     [
#         sum(m1[i][j]*m2[k][j] for k in range(2))
#         for j in range(2)
#     ]
#     for i in range(2)
# ]


# students = [
#     [80, 90, 85],   # Student 1
#     [70, 75, 80],   # Student 2
#     [60, 65, 70]    # Student 3
# ]
# t=0
# c=0

# for i in students:
#     for m  in i:
#         t+=m
#         c+=1
# print(t/c)

# for i,student in enumerate(students):
#     avg=sum(student)/len(student)
#     print(f"{i+1} {avg}")


# a12=[[1,2,3],[4,5,6]]
# a13=[[1,2,3],[5,6,7]]
# res13=np.cross(a12,a13)
# print(res13)


# print(res12)


Aa=np.array([[1,2],
            [4,2]])

# cov=np.cov(Aa.T)
# e_values,e_vectors=np.linalg.eig(cov)
# print("hello")
# print(e_values,e_vectors)
# e_values,e_vectors=np.linalg.eig(Aa)
# print("HIII")
# print(e_values,e_vectors)


# arr112=np.array([[2,3,4],
#         [3,5,6,]])

# covv1=np.cov(arr112.T)

# e_val,e_vect=np.linalg.eig(covv1)
# print(e_val,e_vect)


# ex1=np.array([[3,0],
#              [0,2]])

# e_values,e_vectors=np.linalg.eig(ex1)
# print(e_values)
# print(e_vect)


# d12=np.array([
#     [80,85],
#     [70,75],
#     [60,65]
    
# ])
# mean = np.mean(d12,axis=0)
# centerd=d12-mean
# cov=np.cov(centerd.T)
# e_val,e_vec=np.linalg.eig(cov)
# print(e_val,e_vec)

# d12=np.array([
#     [80,60],
#     [70,75],
#     [60,90]
# ])

# mean=np.mean(d12)
# centerd=d12-mean
# cov=np.cov(centerd.T)

# e_val,e_vect=np.linalg.eig(cov)
# print(e_val,e_vect)



# A=np.array([[1,2],
#             [3,4],
#             [4,3]])

# B=np.array([[1,2,6],
#             [3,5,8],
#             [2,3,0],
#             [5,6,5]])

# C=np.cross(A,B)
# print(C)
# D=np.linalg.matrix_rank(B)
# print(D)


A=np.array([
    [1,2],
    [3,5]
])
print(np.linalg.matrix_rank(A))

B=np.array([6,8,2])

print(np.linalg.norm(B))

A=np.array([[1,2,3],[4,2,2]])
print(np.linalg.svd(A))