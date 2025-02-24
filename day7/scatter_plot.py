import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', marker='<') #'o': Circle (default),'s': Square,'^': Triangle up,'v': Triangle down,'>': Triangle right'<': Triangle lef
#'d': Diamond,'p': Pentago,'H': Hexagon (regular),'X': X (cross),'+': Plus sign,'.': Point (small dot),',': Pixel (even smaller dot),'|': Vertical line,'_': Horizontal line
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()