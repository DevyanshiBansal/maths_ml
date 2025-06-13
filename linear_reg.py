

import numpy as np

# Sample dataset
X = np.array([1, 2, 3, 4, 5])  # House sizes
y = np.array([100, 200, 300, 400, 500])  # House prices

# Initialize parameters
w = 0
b = 0
learning_rate = 0.01
epochs = 100

# Gradient Descent
for epoch in range(epochs):
    # Compute predictions
    predictions = w * X + b
    
    # Compute gradients
    dw = (1/len(X)) * np.sum((predictions - y) * X)
    db = (1/len(X)) * np.sum(predictions - y)
    
    # Update parameters
    w -= learning_rate * dw
    b -= learning_rate * db

print("Optimal parameters: w =", w, "b =", b)

