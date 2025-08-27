import numpy as np

if __name__ == "__main__":
  arr1 = np.array([1, 2, 3, 4, 5, 3, 5, 3])
  arr2 = np.where(arr1 == 3)
  print(f"Found [3] at following indexes: {arr2}")

  arr3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
  arr4 = np.where(arr3 % 2 == 0)
  print(f"Even numbers indexes: {arr4}")
  arr5 = np.where(arr3 % 2 == 1)
  print(f"Odd numbers indexes: {arr5}")

  arr6 = arr3.searchsorted(7)
  print(f"[7] should be inserted at index: {arr6}")

  arr7 = np.searchsorted(arr3, 7, side="right")
  print(f"From right side [7] should be inserted at index: {arr7}")

  arr8 = np.array([1, 3, 5, 7, 9])
  arr9 = np.searchsorted(arr8, [2, 4, 6, 8])
  print(f"[2, 4, 6, 8] should be inserted at indexes: {arr9}")

