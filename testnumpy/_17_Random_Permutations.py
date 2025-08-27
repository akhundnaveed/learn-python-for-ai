from numpy import random
import numpy as np

if __name__ == "__main__":
  # A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
  arr1 = np.array([1, 2, 3, 4, 5])
  random.shuffle(arr1) # Shuffles original array
  print(f"Shuffled Array:\n{arr1}")

  arr2 = np.array([1, 2, 3, 4, 5])
  print(f"\nShuffled array: {random.permutation(arr2)}") # returns a copy of shuffled array

  
