import numpy as np

if __name__ == "__main__":
  arr1 = np.array([1, 2, 3, 4])
  arr2 = arr1.copy() # Deep copy

  arr2[2] = 5
  print(arr1)
  print(arr2) # 3rd element should be different

  arr3 = arr1.view()

  arr3[3] = 6
  print(arr1)
  print(arr3) # Both arrays should exactly be same

  print(arr1.base)
  print(arr3.base)
