import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == "__main__":
  # sns.displot([0, 1, 2, 3, 4, 5])
  sns.displot([0, 1, 2, 3, 4, 5], kind='kde')
  
  plt.show()
