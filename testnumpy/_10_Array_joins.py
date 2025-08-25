import numpy as np

if __name__ == "__main__":
  arr1 = np.array([1, 2, 3, 4])
  arr2 = np.array([5, 6, 7, 8])
  arr3 = np.concatenate((arr1, arr2))
  print(arr3)

  # 2-D arrays joining
  print("\nJoin 2D array")
  arr4 = np.array([[1, 2], [3, 4]])
  arr5 = np.array([[5, 6], [7, 8]])
  arr6 = np.concatenate((arr4, arr5), axis=1)
  print(arr6)

  # Stacking
  print("\nStack")
  arr7 = np.stack((arr1, arr2), axis=1)
  print(arr7)

  # Stacking along rows
  print("\nStacking along rows")
  arr8 = np.hstack((arr1, arr2))
  print(arr8)

  # Stacking along columns
  print("\nStacking along columns")
  arr9 = np.vstack((arr1, arr2))
  print(arr9)

  # Stacking along height (depth) - So here the depth is 4, it'll make its height to 4
  print("\nStacking along height (depth)")
  arr10 = np.dstack((arr1, arr2))
  print(arr10)


