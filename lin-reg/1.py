
import numpy as np
x = np.array([1,2,3])
y = np.array([100,200,300])

learning_rate = 0.01
w = 0
b = 0
i = 0

steps=100

for step in range(steps):
    sum1=0
    sum2=0
    
    for i in range(3):
        x_index = x[i]
        y_index = y[i]

        prediction = w * x_index + b
        formula1 = (prediction - y_index) * x_index
        sum1+=formula1

        formula2 = (prediction - y_index)
        sum2+=formula2

    dw = (1/len(x)) * sum1
    
    db = (1/len(x)) * sum2

    w-= learning_rate * dw
    b-= learning_rate * db

print(f"w : {w}")
print(f"b : {b}")