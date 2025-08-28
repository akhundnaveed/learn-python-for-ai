from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == "__main__":
  # loc = mean = peak of the bell
  # scale = standard deviation
  x = random.normal(loc=1, scale=2, size=(2, 3))
  print(x)

  # sns.displot(x, kind='kde')
  # plt.show()

  sns.displot(random.normal(size=1000), kind='kde')
  plt.show()
