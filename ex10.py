import numpy as np

def pseudo_rand(x):
    a = 1103515245
    b = 12345
    m = 2 ** 31
    new_x = (a * x + b) % m
    return new_x
seed = 100
x = pseudo_rand(seed)
print(x)
x = pseudo_rand(x)
print(x)

rnd = np.random.randn(5) * 10 + 165
print(rnd)
a = rnd.round(2)
print(a)
b = rnd.astype(int)
print(b)
nums = np.random.normal(loc =165, scale = 10, size=(3,4)).round(2)
print(nums)
X = np.arange(50)
np.random.shuffle(X)
print(X)