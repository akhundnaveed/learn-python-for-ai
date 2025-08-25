import numpy as np

if __name__ == "__main__":
  # Split into 2 arrays
  arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
  arr1 = np.array_split(arr, 2)
  print(arr1)

  # Split into 5 arrays, adjust the values according
  arr2 = np.array_split(arr, 5)
  print(arr2)
  print(f"arr[2]: {arr2[2]}")

  try:
    arr3 = np.split(arr, 5)
  except:
    print("Cannot split 8 elements into 5 arrays")

  # Split 2-D arrays
  print("\nSplit 2-D array")
  arr4 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
  arr5 = np.array_split(arr4, 3)
  print(arr5)

  # Split 2-D array into 3 2-D arrays with axis
  print("\nSplit 2-D array into 3 2-D arrays")
  arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
  arr7 = np.array_split(arr6, 3, axis=0)
  print(arr7)

  # Split horizontal
  print("\nH Split")
  arr8 = np.hsplit(arr6, 3)
  print(arr8)
