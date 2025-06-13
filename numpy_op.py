
import numpy as np

arr = np.random.randint(50,size = [4,3]) # chooses random numbers from 0 to 50 and makes a matrix of size 4x3
print(arr)

# operations on numoy

a = np.array([[2,3,4]])
b = np.array([[5,6,7]])

# one way to use operations
add = print(f"add is : {np.add(a,b)}")
sub = print(f"sub is : {np.subtract(a,b)}")
multiply = print(f"mul. is : {np.multiply(a,b)}")
divide = print(f"div. is : {np.divide(a,b)}")

c = np.array([[22,3,4,],[32,55,6],[17,99,7]])
d = np.array([[11,23,44],[8,9,10],[66,5,2]])

# other way to use operations 
x = c+d
print(x)
print(np.add(c,d))
# both ways can we used for operations

print(c-d)
print(c*d)

print(np.dot(c,d)) # matrix multiplication
print()
print(np.cross(c,d)) 

t = np.transpose(c) # transpose
print(t)

zero = np.zeros((5,3),dtype=int)
print(zero)

print(c[2,1])