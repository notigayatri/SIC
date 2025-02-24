import matplotlib.pyplot as plt
import numpy as np

data = [np.random.randn(100) for _ in range(4)]
plt.violinplot(data)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()