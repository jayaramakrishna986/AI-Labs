# from sklearn.tree import DecisionTreeRegressor
# import numpy as np

# X=np.array([[1],[2],[3],[4]])
# y=[1,4,9,16]

# model=DecisionTreeRegressor()
# model.fit(X,y)

# print(model.predict([[5]]))

# import pandas as pd
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.metrics import mean_squared_error
# from sklearn.model_selection import train_test_split



# df=pd.read_csv("BostonHousing.csv")

# X=df.drop("medv",axis=1)
# y=df["medv"]


# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


# model=DecisionTreeRegressor()
# model.fit(X_train,y_train)

# y_pred=model.predict(X_test)

# print("Mean Square error:",mean_squared_error(y_test,y_pred))


# # Classifier
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score

# # Load 
# # datase
# df = pd.read_csv(
#     "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/sms.tsv",
#     sep="\t",
#     header=None
# )




# df.columns = ["label", "message"]


# # df["label"]=df["label"].map("ham":0,"spam":1)
# # Convert labels
# df["label"] = df["label"].map({"ham": 0, "spam": 1})

# # Convert text to numbers
# from sklearn.feature_extraction.text import CountVectorizer

# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(df["message"])
# y = df["label"]

# # Split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Model
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# # Prediction
# y_pred = model.predict(X_test)

# # Evaluation
# print("Accuracy:", accuracy_score(y_test, y_pred))


#Logistic regression

from sklearn.linear_model import LogisticRegression

X=[[1],[2],[3],[4]]
y=[0,0,1,1]

model=LogisticRegression()
model.fit(X,y)
print(model.predict([[2.4]]))
print(model.predict_proba([[2.5]]))

# Z score 
import numpy as np
import pandas as pd

data = {"price": [200, 220, 250, 270, 300, 1000]}
df = pd.DataFrame(data)

# Mean and std
mean = np.mean(df["price"])
std = np.std(df["price"])

# Z-score
df["z_score"] = (df["price"] - mean) / std

# Filter outliers
df_clean = df[np.abs(df["z_score"]) < 3]

print(df_clean)