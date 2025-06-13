
import numpy as np
 
a = np.array([1,2,3,4])

# mean
mean1 = np.mean(a)
print(mean1)

# this same thing can be done for standard deviation and variance when 2d array is given 

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
mean2 = np.mean(b , axis=0)
mean3 = np.mean(b , axis=1)

print(mean2)
print(mean3)

print(mean2[0] ,"\t", mean2[1] ,"\t", mean2[2],"\t", end = " ") 

print(mean3[0] ,"\t", mean3[1] ,"\t", mean3[2],"\t", end = " ") 

print()

# variance

variance = np.var(a)
print(variance)
# similarly can be done for b as b was done for mean


# standard deviartion 
# it is square root of variance and tell us how far data is from mean

sd = np.std(a)
print(sd)

# similarly can be done for b as b was done for mean

# median

med1 = np.median(a) # for even no. of digits
print(med1)

c = np.array([1,2,3,4,5])

med2 = np.median(c) # for odd no. of digits
print(med2)

med3 = np.median(b,axis=0)

print(med3[0] ,"\t", med3[1] ,"\t", med3[2],"\t", end = " ") 

print(med3[0] ,"\t", med3[1] ,"\t", med3[2],"\t", end = " ") 