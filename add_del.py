
import numpy as np

a = np.array([[1,2,3],[5,4,9],[9,8,11]])
b = np.array([[10,20,30]]) 
m = b[0]
print(m)

# adding a row or column

# vstack
v = np.vstack([a,b]) # in vstack we need equal no. of columns
print(v)

# hstack
# in hstack we need equal no. of rows as 
h = np.hstack((a, np.atleast_2d(b).T)) 
print(h)

 # atleast_2d if a function which converts 1d array to 2d. 
 # here first by using atleast_2d b was made into a (1,3) 2d array and then by transpose it converts to (3,1) ie 3 rows which is equal to rows as a 

# deleting a row or column

deletion1 = np.delete(a,0,axis = 1)
print(deletion1)

deletion2 = np.delete(a,0,axis = 0)
print(deletion2)