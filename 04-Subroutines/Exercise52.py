# 52.	Define a function power(x, n) that calculates xn. 
# Apply recursion. 
# Then, calculate 53.
# Tip: x^n =  x * x^(n-1)

import topower

x = 5
n = 3
result = topower.power(x, n)
print(f"f({x, n}) returns {result}")

x = 4
n = 0
result = topower.power(x, n)
print(f"f({x, n}) returns {result}")

x = 2
n = 4
result = topower.power(x, n)
print(f"f({x, n}) returns {result}")