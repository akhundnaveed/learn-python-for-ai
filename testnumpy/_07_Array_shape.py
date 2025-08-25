import numpy as np

if __name__ == "__main__":
  arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
  print(arr.shape) # (2, 4) means 2-D array, first dimension has 2 elements and second dimension has 4

  arr1 = np.array(arr[0], ndmin=5)
  print(arr1.shape) # (1, 1, 1, 1, 4)
