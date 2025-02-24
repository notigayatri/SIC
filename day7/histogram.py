import matplotlib.pyplot as plt
import numpy as np 

data = np.random.randn(1000)

plt.hist(data, bins=30, color='green', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()