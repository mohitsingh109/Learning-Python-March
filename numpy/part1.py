import numpy as np

x = np.array([1, 2, 3, 4])
print(x)
print(type(x))
print(x.dtype)

# y = [1, 2, 3, 4]
# print(y)
# print(type(y))

# Python all any data to be stored but numpy all datatype should be same
p_l1 = ["One", 2, 4, False]
print(p_l1)

# Broadcasting
x = x * 2
print(x)

# 2D Numpy
p_matrix = [[1,2],
           [3,4]]
np_matrix = np.array([[1, 2],[3, 4],[5, 6]])
print(np_matrix)
print("Shape:", np_matrix.shape)
print("Dim:", np_matrix.ndim)

# Math function

arr = np.array([1, 2, 3, 4])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))

# How to view shape
print("Shape:", arr.shape)
# How to view dimension
print("Dim:", arr.ndim)

