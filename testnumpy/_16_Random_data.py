from numpy import random

if __name__ == "__main__":
  # Data Distribution is a list of all possible values, and how often each value occurs.
  arr = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=100)
  print(f"Random choice array with defined probabilities:\n{arr}")
  # It means out of 100 numbers, 3 would occur 10 times, 5 would occur 30 times,
  # 7 would occur 60 times and 9 would never appear as its probability is 0.0

  arr1 = random.choice([2, 4, 6, 8], p=[0.3, 0.3, 0.2, 0.2], size=(5, 10))
  print(f"\nRandom choice 2-D array with defined probabilities:\n{arr1}")
  # Note: sum of all probabilities should be 1 otherwise it'll throw error
