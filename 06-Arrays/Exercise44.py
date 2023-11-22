# 44.	Write a program that draws the graph of the function f(x)=x^2-3. 
# Sample result:

import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100, 101):
    x.append(n)

# create y values
for n in x:
    y.append(n**2 - 3)

# display chart
plt.title("Function graph")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()