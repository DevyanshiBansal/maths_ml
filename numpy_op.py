
import numpy as np

arr = np.random.randint(50,size = [4,3]) # chooses random numbers from 0 to 50 and makes a matrix of size 4x3
print(arr)

# operations on numoy

a = int(input())
b = int(input())

add = print(f"add is : {np.add(a,b)}")
sub = print(f"sub is : {np.subtract(a,b)}")
multiply = print(f"sub is : {np.multiply(a,b)}")
divide = print(f"sub is : {np.divide(a,b)}")

c = np.array([[22,3,4,],[32,55,6],[54,5,99]])
d = np.array([[11,23,44],[8,9,10],[17,99,7]])

print(np.dot(c,d)) # matrix multiplication
print()
print(np.cross(c,d)) # find determinant type

t = np.transpose(c) # transpose
print(t)

zero = np.zeros((5,3),dtype=int)
print(zero)

print(c[2,1])