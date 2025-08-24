import numpy as np

# 1-D array
arr = np.array([1, 2, 3, 4])
print(f"{arr[1] + arr[2]} == 5: {(arr[1] + arr[2]) == 5}")

# 2-D array
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"{arr1[0, 1] + arr1[1, 3]} == 10: {(arr1[0, 1] + arr1[1, 3]) == 10}")

# 3-D array
arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"{arr2[0, 0, 1]} + {arr2[0, 1, 1]} + {arr2[1, 1, 1]} = 14: True")

# Negative index - means access from end
arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"{arr3[0, -1]} = 4, {arr3[-1, -2]} = 7")

