import copy, math
import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('./deeplearning.mplstyle')
# np.set_printoptions(precision=2)  # reduced display precision on numpy arrays


X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])


# data is stored in numpy array/matrix
print(f"X Shape: {X_train.shape}, X Type:{type(X_train)})")
print(X_train)
print(f"y Shape: {y_train.shape}, y Type:{type(y_train)})")
print(y_train)


b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
print(f"w_init shape: {w_init.shape}, b_init type: {type(b_init)}")


def predict_single_loop(x, w, b): 
    """
    single predict using linear regression
    
    Args:
      x (ndarray): Shape (n,) example with multiple features
      w (ndarray): Shape (n,) model parameters    
      b (scalar):  model parameter     
      
    Returns:
      p (scalar):  prediction
    """
    n = x.shape[0]
    p = 0
    for i in range(n):
        p_i = x[i] * w[i]  
        p = p + p_i         
    p = p + b                
    return p

# get a row from our training data
x_vec = X_train[0,:]
print(f"x_vec shape {x_vec.shape}, x_vec value: {x_vec}")

# make a prediction
f_wb = predict_single_loop(x_vec, w_init, b_init)
print(f"f_wb shape {f_wb.shape}, prediction: {f_wb}")

def predict(x, w, b): 
    """
    single predict using linear regression
    Args:
      x (ndarray): Shape (n,) example with multiple features
      w (ndarray): Shape (n,) model parameters   
      b (scalar):             model parameter 
      
    Returns:
      p (scalar):  prediction
    """
    p = np.dot(x, w) + b     
    return p    

# get a row from our training data
x_vec = X_train[0,:]
print(f"x_vec shape {x_vec.shape}, x_vec value: {x_vec}")

# make a prediction
f_wb = predict(x_vec,w_init, b_init)
print(f"f_wb shape {f_wb.shape}, prediction: {f_wb}")


# 5.1 Compute Gradient with Multiple Variables
# An implementation for calculating the equations (6) and (7) is below. There are many ways to implement this. In this version, there is an

# outer loop over all m examples.
# ∂𝐽(𝐰,𝑏)∂𝑏
#   for the example can be computed directly and accumulated
# in a second loop over all n features:
# ∂𝐽(𝐰,𝑏)∂𝑤𝑗
#   is computed for each  𝑤𝑗
#  .

def compute_gradient(X, y, w, b): 
    """
    Computes the gradient for linear regression 
    Args:
      X (ndarray (m,n)): Data, m examples with n features
      y (ndarray (m,)) : target values
      w (ndarray (n,)) : model parameters  
      b (scalar)       : model parameter
      
    Returns:
      dj_dw (ndarray (n,)): The gradient of the cost w.r.t. the parameters w. 
      dj_db (scalar):       The gradient of the cost w.r.t. the parameter b. 
    """
    m,n = X.shape           #(number of examples, number of features)
    dj_dw = np.zeros((n,))
    dj_db = 0.

    for i in range(m):                             
        err = (np.dot(X[i], w) + b) - y[i]   
        for j in range(n):                         
            dj_dw[j] = dj_dw[j] + err * X[i, j]    
        dj_db = dj_db + err                        
    dj_dw = dj_dw / m                                
    dj_db = dj_db / m                                
        
    return dj_db, dj_dw


import numpy as np

X=np.array([[1],[2],[3],[4],[5]])
y = np.array([3, 6, 9, 12, 15])  # y = 3x

w=np.zeros(1)
b=0

alpha=0.1
iterations=1000
# print(X.shape[0])
# Gradient function
def compute_gradient(X,y,w,b):
    m=X.shape[0]

    predictions=np.dot(X,w)+b

    error=predictions-y

    dj_dw=(1/m)*np.dot(X.T,error)
    dj_db=(1/m)*np.sum(error)

    return dj_dw,dj_db
#Cost function
def compute_cost(X,y,w,b):
    m=X.shape[0]
    predictions=np.dot(X,w)+b

    cost=(1/(2*m)) *np.sum((predictions-y)**2)

    return cost
#Gradient Descent Loop
for i in range(iterations):

    # Calculate gradients
    dj_dw, dj_db = compute_gradient(X, y, w, b)

    # Update parameters
    w = w - alpha * dj_dw
    b = b - alpha * dj_db

    # Print progress every 100 steps
    if i % 100 == 0:
        cost = compute_cost(X, y, w, b)
        print(f"Iteration {i}: Cost={cost:.4f}, w={w}, b={b}")


print("\nFinal Parameters:")
print("w =", w)
print("b =", b)

x_test = np.array([6])
prediction = np.dot(x_test, w) + b

print(f"\nPrediction for x=6: {prediction}")