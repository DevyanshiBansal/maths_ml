
import numpy as np

l1 = [1,2,3,4] # 1d list horizontal
v1 = np.array(l1) 
print(v1)

l2 = [[10],
      [20],
      [30]]  # 1d vertical list

v2 = np.array(l2)
print(v2)

# addition of vectors

# this is actually like addition of 1d arrays only

l3 = [1,2,3]
v3 = np.array(l3)

l4 = [12,13,14]
v4 = np.array(l4)

addition = v1 + v2 # so this is a case of broadcasting
print(addition)

addition2 = v3+v4
print(addition2) # this is basic addition

multiplication = v1*v2 # again broadcating takes place here.
print(multiplication)

mult2 = v3*v4 # multiplication of vectors element to element
print(mult2)

# like addition only all other operations take place

# dot product

dot_product = v3.dot(v4)
print(dot_product) # a1b1+a2b2 +a3b3

# vector scalar multiplication

scalar = 10

v_s = v2*scalar # we can write v1,v3,v4 anything
# in this scalar multiplies to all the elements  
print(v_s)
