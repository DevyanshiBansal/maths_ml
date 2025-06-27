

import numpy as np

# Sample dataset
X = np.array([1, 2, 3, 4, 5])  # House sizes
y = np.array([100, 200, 300, 400, 500])  # House prices

# Initialize parameters
w = 0
b = 0
learning_rate = 0.01
epochs = 1

# Gradient Descent
for epoch in range(epochs):
    # Compute predictions
    predictions = w * X + b
    print(predictions.shape)  # it is an array of order (5,1)
    
    # Compute gradients 

    dw = (1/len(X)) * np.sum((predictions - y) * X) # the multiplication sign here does element-wise multiply not dot or cross product.

    # so here in dw, two arrays are subtracted like elements are subtracted which then gives one array which is them element wise multiplied to X array.
    db = (1/len(X)) * np.sum(predictions - y)
    
    # Update parameters
    w -= learning_rate * dw
    b -= learning_rate * db

print("Optimal parameters: w =", w, "b =", b) 

# np.sum((predictions - y) * X) this whole thing acts like a submission and same for db one.