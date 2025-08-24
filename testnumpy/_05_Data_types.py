import numpy as np

if __name__ == "__main__":
  arr = np.array((1, 2, 3, 4, 5))
  print(arr.dtype)

  sarr = np.array(["apple", "banana", "watermelon", "cherry"])
  print(sarr.dtype)
  k = 2.1j # Complex datatype
  i = 2.1 # Float datatype
  print(f"k.type={type(k)}, i.type={type(i)}")

  arr1 = np.array([1, 2, 3, 4], dtype='S')
  print(arr1.dtype) # S1 means 1 byte string

  try:
    arr2 = np.array(['1', 'a', 'x'], dtype='i1') # ValueError: cannot convert to integer
  except ValueError as e:
    print(e)

  arr3 = np.array([1.1, 2.2, 3.3, 4.4])
  arr4 = arr3.astype('i') # Convert float to integer
  print(arr4)
  print(arr4.dtype)

  arr5 = arr3.astype(int) # other way to convert float to integer
  print(arr5)
  print(arr5.dtype)

  arr6 = np.array([1, 0, 3, -1], dtype=bool)
  print(arr6)
  print(arr6.dtype)

