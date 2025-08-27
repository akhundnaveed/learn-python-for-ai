import numpy as np

if __name__ == "__main__":
  arr = np.array([3, 2, 0, 1])
  print(f"\nNumber array sorted:\n{np.sort(arr)}")

  sarr = np.array(['grapes', 'dragonfruit', 'banana', 'cherry', 'apple'])
  print(f"\nString array sorted:\n{np.sort(sarr)}")

  barr = np.array([[True, False, True]])
  print(f"\nBoolean array sorted:\n{np.sort(barr)}")

  arr2 = np.array([[4, 3, 2], [5, 6, 1]])
  print(f"\n2-D Array sorted:\n{np.sort(arr2)}")

