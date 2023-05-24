import numpy as np

a = np.array([[70, 10],[40, 50]])
b = np.array([[45, 74],[75, 84]])
c = np.matmul(a, b)
print(a @ b)
print(c)

d = np.arange(12)
print(d)
print(d.reshape(3,4))