# import numpy as np
# import pandas as pd
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt


# data = {
#     'Math': [90, 60, 75, 85, 50],
#     'Physics': [85, 65, 70, 80, 55],
#     'Chemistry': [88, 63, 72, 82, 58]
# }

# df = pd.DataFrame(data)


# scalar=StandardScaler()
# scaled_data=scalar.fit_transform(df)

# pca=PCA(n_components=2)
# principal_components=pca.fit_transform(scaled_data)

# print(principal_components)

# print(pca.explained_variance_)

# plt.scatter(principal_components[:,0],principal_components[:,1])

# plt.xlabel("PC1")
# plt.xlabel("PC2")
# plt.show()


# PCA

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

data = {
    'Math': [90, 60, 75, 85, 50],
    'Physics': [85, 65, 70, 80, 55],
    'Chemistry': [88, 63, 72, 82, 58]
}

df = pd.DataFrame(data)

# Step 1: Standardize
scaler = StandardScaler()
scaled = scaler.fit_transform(df)

# Step 2: Apply PCA
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled)

# PC1 and PC2 values
print(pca_data)

# Importance
print(pca.explained_variance_ratio_)

# Directions (IMPORTANT)
print(pca.components_)


#XGBoost 

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data=load_iris()
X,y = data.data ,data.target
X_train,X_test,y_train,y_test=train_test_split(X,y)

model=XGBClassifier(n_estimars=100,learning_rate=0.1)

model.fit(X_train,y_train)
preds=model.predict(X_test)
print(y_test)
print(preds)