import numpy as np

if __name__ == "__main__":
  arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
  arr1 = arr.reshape(3, 4)
  print(arr1)

  arr2 = arr.reshape(2, 3, 2)
  print(arr2)

  try:
    arr3 = arr.reshape(3, 3)
  except:
    print("Error while reshaping") # Should run

  print(arr.reshape(3, 4).base) # Here base propery returns the actual array, which means reshape returns view and not a copy/deep copy

  # We can specify -1 for on unknow dimention
  arr4 = arr.reshape(2, 2, -1) # We cannot pass -1 for more than one dimensions
  print(arr4.shape)

  # Flattening the multi dimension array to single dimension
  arr5 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
  arr6 = arr5.reshape(-1)
  print(arr6)

  arr7 = arr5.flatten() # Another way to flatten the array
  print(arr7)

  arr8 = arr5.ravel()
  print(arr8)
