import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10,10)  # Generate a 10x10 matrix of random values

# Create heatmap
plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap")
plt.show()