import numpy as np

a = np.array([2,3,4,5,6,6])
b = np.array([1,2])
a[2-2:2+2+1]+=1
print(a)
print(np.all(a==[2, 4, 5, 5 ,6 ,6]))