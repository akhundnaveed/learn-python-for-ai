import numpy as np

if __name__ == "__main__":
  # = [+ Index] > 0, 1, 2, 3, 4, 5, 6
  arr = np.array((1, 2, 3, 4, 5, 6, 7))
  # = [- Index] > -7,-6,-5,-4,-3,-2,-1
  print(arr[1:5]) # [2 3 4 5]
  print(arr[4:]) # [5 6 7]
  print(arr[:3]) # [1 2 3]

  # Negative Slicing
  print(arr[-4:-1]) # [4 5 6]
  print(arr[-7:-4]) # [1 2 3]

  # Steps
  print(arr[1:5:2]) # [2 4]
  print(arr[::2]) # [1 3 5 7]
  print(arr[1::2]) # [2 4 6]

  # 2-D Array Slicing
  arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
  # Take 2 index element of both arrays
  print(arr1[0:2, 2]) # [3 8]
  # Take 1 to 4 from both arrays
  print(arr1[:, 1:4]) # [[2 3 4] [7 8 9]]
