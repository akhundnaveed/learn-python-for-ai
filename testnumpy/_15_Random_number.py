from numpy import random

if __name__ == "__main__":
  n = random.randint(100)
  print(f"Random Int:\n{n}")

  f = random.rand()
  print(f"\nRandom Float:\n{f}")

  iarr = random.randint(100, size=8)
  print(f"\nRandom Int Array:\n{iarr}")

  iarr1 = random.randint(100, size=(2, 3))
  print(f"\nRandom Int 2-D Array:\n{iarr1}")

  farr = random.rand(5)
  print(f"\nRandom Float Array:\n{farr}")

  farr1 = random.rand(2, 3)
  print(f"\nRandom Float 2-D Array:\n{farr1}")

  n = random.choice([1, 2, 5, 6, 9, 10])
  print(f"\nRandom number from given choice array:\n{n}")

  arrc = random.choice([1, 2, 5, 6, 9, 10], size=(3, 2))
  print(f"\nRandom 2-D array from given choice array:\n{arrc}")
