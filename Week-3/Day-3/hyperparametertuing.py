from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
#grid Search
model = RandomForestClassifier()
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 5]
}

grid=GridSearchCV(model,param_grid,cv=5)
grid.fit(X_train,y_train)

print(grid.best_params_)
print(grid.best_score_)

param_dist = {
    'n_estimators': [100, 200, 300, 400],
    'max_depth': [3, 5, 7, 10]
}
# 👉 Instead of 16 combinations, it might try:
# (200, 7)
# (400, 3)
# (100, 10)

from sklearn.model_selection import RandomizedSearchCV

random = RandomizedSearchCV(
    model,
    param_distributions=param_dist,
    n_iter=5,   # number of random tries
    cv=5
)

random.fit(X_train, y_train)

print(random.best_params_)

# ✅ Advantages

# ✔️ Faster
# ✔️ Works well in large search space

random = RandomizedSearchCV(
    model,
    param_distributions=param_dist,
    n_iter=5,
    cv=5,
    n_jobs=-1,   # use all CPU cores
    random_state=42
)