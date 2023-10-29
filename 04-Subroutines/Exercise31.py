# 31.	Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. 
# Sample result:
# f(-7,8) returns 3
# f(-1,11) returns 0

import negativeeven

x = -7
y = 8
sum = negativeeven.f(x,y)
print(f"f({x}, {y}) returns {sum}")

x = -1
y = 11
sum = negativeeven.f(x,y)
print(f"f({x}, {y}) returns {sum}")