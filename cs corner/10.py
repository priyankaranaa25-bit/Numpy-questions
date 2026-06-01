import numpy as np
a=np.array([[10,20,30],[40,50,60]])
print (a)
print("shape:",a.shape)
print("size:",a.size)
print("ndim:",a.ndim)
print("dtype:",a.dtype)
b=a.astype(float)
print(b)