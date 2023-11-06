# 42.	Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers.
# Sample result:
# f(7,4,9) returns 5
# f(2,12,8) returns 10

import numberdifference


number1 = 7
number2 = 4
number3 = 9
difference = numberdifference.f(number1,number2,number3)
print(f"f({number1}, {number2}, {number3}) returns {difference}")

number1 = 2
number2 = 12
number3 = 8
difference = numberdifference.f(number1,number2,number3)
print(f"f({number1}, {number2}, {number3}) returns {difference}")