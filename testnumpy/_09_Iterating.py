import numpy as np

if __name__ == "__main__":
  # Iterate 1-D
  arr = np.array([1, 2, 3])
  for n in arr:
    print(n)


  # Iterate 2-D
  print("\n2D array")
  arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
  for n in arr1:
    for n1 in n:
      print(n1)


  # Iterate 3-D
  print("\n3D array")
  arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
  for n1 in arr2:
    for n2 in n1:
      for n3 in n2:
        print(n3)

  # Using nditer to iterate n-dimensions of array.
  print("\nUsing nditer")
  for x in np.nditer(arr2):
    print(x)

  # Change datatype. Not in place. Using Buffer for temp space for chaning the datatype
  print("\nChange datatype")
  for x in np.nditer(arr2, flags=['buffered'], op_dtypes=['S']):
    print(x)

  print("\nSkip 1 element")
  for n in np.nditer(arr1[:, 1::2]):
    print(n)

  # Iterate with index
  for idx, n in np.ndenumerate(arr2):
    print(f"[{idx}] {n}")
