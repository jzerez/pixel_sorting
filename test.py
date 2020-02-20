import numpy as np
a = np.array([1,2,3,4,5,2,3,1])
def foo(arr):
    for i, elem in enumerate(a):
        a[i] = elem * 2
    return a

print(a)
print(foo(a))
print(a)
