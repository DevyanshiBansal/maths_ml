
import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([3,8,9,7,2,1])

# covariance varies from -inf to +inf.
cov1 = np.cov(a,b)
print(cov1) # this gives a matrix whose off side matrix is the actual covariance
print(cov1[0,1]) # this gives the actual value of covariance from 0th row 1st colum of the covar nmatrix


# it ranges from -1 to 1 
corcoff = np.corrcoef(a,b)
print(corcoff) # this gives a matrix whose off side matrix is the actual covariance
print(corcoff[0,1]) # this gives the actual value of covariance from 0th row 1st colum of the covar nmatrix