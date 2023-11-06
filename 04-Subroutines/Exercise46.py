# 46.	Define the function f(x,y), which returns the sum of numbers in the range <x,y> that are completely divisible by 2 and 3 and not divisible by 4. 
# Sample result:
# f(1,20) returns 24
# f(10,30) returns 48

import sumofnumbersinrange

x = 1
y = 20
sum = sumofnumbersinrange.f(x,y)
print(f"f({x},{y}) returns {sum}")

x = 10
y = 30
sum = sumofnumbersinrange.f(x,y)
print(f"f({x},{y}) returns {sum}")