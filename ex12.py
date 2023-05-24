import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = [i for i in np.linspace(0,10,1000)]
print(x)
y = [i ** 2 for i in x]
print(y)
plt.plot(x, y, 'o')
plt.show()