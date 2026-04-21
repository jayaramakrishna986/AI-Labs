# 🔥 1. What is Cross Validation?

# 👉 Cross Validation is a technique to:

# ✔️ Evaluate model performance
# ✔️ Ensure model works well on unseen data
# Instead of using one train-test split, we use multiple splits to get a more reliable result

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load data
data = load_iris()
X, y = data.data, data.target

# Model
model = RandomForestClassifier()

# Cross validation
scores = cross_val_score(model, X, y, cv=5)

print(scores)
print("Average:", scores.mean())