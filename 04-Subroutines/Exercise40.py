# 40.	Define a function f(number) that returns the sum of repeated digits in a number. 
# Sample result:
# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21 

import sumofnumbers

number = "1027"
sum_of_repeated_digits = sumofnumbers.f(number)
print(f"f({number}) returns {sum_of_repeated_digits}")

number = "230335"
sum_of_repeated_digits = sumofnumbers.f(number)
print(f"f({number}) returns {sum_of_repeated_digits}")

number = "513553007"
sum_of_repeated_digits = sumofnumbers.f(number)
print(f"f({number}) returns {sum_of_repeated_digits}")