
import numpy as np
a = np.matrix('1,2 ; 3,4') # string type input
print(a, "\n")
print(a.T,"\n") # this gives transpose

b = np.matrix([[1,2],[3,4],[5,6]]) # array like input
print(b,"\n") 

ai2 = np.matrix(np.arange(9).reshape(3,3)) # this is also a way to make a matrix with num from 0-9 like here and shape 3X3
print(ai2) 

# functions

multiplication = np.matmul(one,two) # this is matrix multiplication not element wise multiplication
print(multiplication)

# multiplicative inverse is a inverse of matrix which when mmultiplied with the original matrix gives identity matrix

mi = b.getI()
print(mi,"\n")

# getA is a function which converts matrix to a n dimensional array or nd array

ai = b.getA()
print(ai,"\n")

# for sum of matrices

one = np.matrix([[2,3,4],[7,6,5],[22,4,5]])
two = np.matrix([[33,4,2],[54,8,2],[32,4,5]])
add = np.add(one,two)
