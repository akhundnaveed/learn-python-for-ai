from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# n = number of trials
# p = probability
x = random.binomial(n=10, p=0.5, size=1000)

print(x)
# sns.displot(x, kind='hist')
# plt.show()


# Comparison normal vs binomial distirbutions
data = {
  'normal': random.normal(loc=50, scale=5, size=1000),
  'binomial': random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind='kde')
plt.show()
