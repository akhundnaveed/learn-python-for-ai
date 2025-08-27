import numpy as np

if __name__ == "__main__":
  arr1 = np.array([1, 2, 3, 4, 5, 6])
  indx = [False, True, False, True, False, True]
  arr2 = arr1[indx]
  print(f"Filtered Array:\n{arr2}") # [2, 4, 6]

  arr3 = np.array([41, 42, 43, 44, 45])
  filter = []
  for item in arr3:
    if item > 42:
      filter.append(True)
    else:
      filter.append(False)
  
  arr3 = arr3[filter]
  print(f"\nGreater than 42:\n{arr3}")

  filter = arr3 > 41
  arr4 = arr3[filter]
  print(f"\nGreater than 42:\n{arr4}")

