import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

# 0-D array
arr2 = np.array(42)
print(arr2)
print(arr2.ndim, "-D array\n")

# 1-D array
arr1 = np.array((6, 7, 8, 9, 10))

print(arr1)
print(arr1.ndim, "-D array\n")

# 2-D array 2x3
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)
print(arr3.ndim, "-D array\n")

# 3-D array 2 x 2 x 3
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr4)
print(arr4.ndim, "-D array\n")

# 5-D array
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)
print(arr5.ndim, "-D array\n")

