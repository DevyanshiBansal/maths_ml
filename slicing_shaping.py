import numpy as np

data = np.array([[2,3,4,25],[2,5,6,50],[8,9,10,75]])
data[1,1] = 22 
print(data)

a1 = data[0:2] # only row 0 and 1 and but all columns
a2 = data[0:2,:] # same as above colan denote all
a3 = data[0:2,1:3] # slicing both row and column. so here o,1 rows and 1,2 columns
print(a3)

a4 = data[:,3] # this gives all rows with column 3 
print(a4)

a5 = data[2,:] # this gives second row with all columns
print(a5)

a6 = data[0:2,:] # this gives 0,1 rows with all columns
print(a6)

a7 = data[:,1:3] # this gives 1,2 column with all rows 
print(a7)

# this is how slicing is done 
