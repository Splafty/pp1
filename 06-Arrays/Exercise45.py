# 45.	Write a program that draws the function y = sin(x) for an angle value in the range 0-360 degrees.

import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 360 degrees
x = np.arange(0, 361, 1)

# Convert degrees to radians for the sin function
x_rad = np.radians(x)

# Calculate y = sin(x)
y = np.sin(x_rad)

# Plot the function
plt.plot(x, y)
plt.title('Graph of y = sin(x)')
plt.xlabel('Angle (degrees)')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()