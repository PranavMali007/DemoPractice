import numpy as np

a = np.array(((2,2,2),(4,4,4)))
b = np.array(((3,3,3),(4,4,4)))
print(a,'\n')
print(b.T)
print(type(a))
z = np.matmul(a,b.T)
print(z)