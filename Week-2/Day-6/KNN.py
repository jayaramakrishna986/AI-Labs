from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor

X=[[1],[2],[3],[4]]
y=[0,0,1,1]
# classifier
model=KNeighborsClassifier(n_neighbors=2)
model.fit(X,y)
print(model.predict([[2.5]]))

#Regression

y1=[1,4,9,16]

model1=KNeighborsRegressor(n_neighbors=2)

model1.fit(X,y1)

print(model1.predict([[6]]))


from sklearn.svm import SVR,SVC

model2=SVR(kernel='rbf',C=100,epsilon=1)
model2.fit(X,y1)

print(model2.predict([[5]]))

model3=SVC(C=1,kernel='rbf')
model3.fit(X,y)

print(model3.predict([[2]]))