# 13.	In a certain company, 25 employees commute by car, 19 employees commute by public transport, 32 people commute by bike, and 7 people commute on foot. 
# Write a program that displays this data in a bar chart. 
# Remember to add a title for the chart and a description of the chart axes. 
# Sample result:
# See a similar task from the BEFORE CLASS section.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["car", "public transport", "bike", "foot"])
y = np.array([25, 19, 32, 7])

plt.title("Communication choices of employees")
plt.xlabel("Type of transport")
plt.ylabel("Number of employees")
plt.bar(x,y)
plt.show()