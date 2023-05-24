import numpy as np
b = np.array([[1,1],[2,2],[3,3]])
b.sort()
print(b)

c = np.array([3,5,9,1,0])
c.sort()
print(c)
d = np.array([[35,24,55],[69,19,9],[4,1,11]])
d.sort(axis=0)
print(d)