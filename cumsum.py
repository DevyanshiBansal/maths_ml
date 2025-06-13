
# cumsum is a property which gives cumulative sum of the digits till the end.
import numpy as np

a = np.arange(10) # this gives a 1d array of 10 digits ie 0-9
b = np.cumsum(a)

print(a)
print()

print(b)
#  [0,1+0,0+1+2,0+1+2+3 .......] this is how output of b is formed 
