import numpy as np
b = np.array([[1,1], [2,2],[3,3]])
np.insert(b,1,4,axis = 0)
print(b)

#c = [1,3,4]
#c.insert(1,2)
#print(c)
c = np.array([[1,2,3], [4,5,6]])
c = np.flip(c, axis=1)
print(c)

