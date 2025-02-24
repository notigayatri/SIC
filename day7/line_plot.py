import matplotlib.pyplot as plt
import numpy as np
 # Importing 3D plotting module

x = np.linspace(0, 10, 100)  # Generating 100 points between 0 and 10
y = np.sin(x)  # Sine function

plt.plot(x, y, label="Sine Wave")  # Plot sine wave
plt.xlabel("X-axis")  # Label for x-axis
plt.ylabel("Y-axis")  # Label for y-axis
plt.title("Line Plot")  # Title of the plot
plt.legend()  # Display legend
plt.show()  # Show the plot
