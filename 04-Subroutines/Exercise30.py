# 30.	Create a function f(number, even) that computes the sum of the digits of a number. 
# When the value of the even parameter is True, the function returns the sum of the even digits. 
# When the value of the even parameter is False, the function returns the sum of the odd digits. 
# Sample result:
# f(3124,True) returns 6
# f(3124,False) returns 4
# f(20576,False) returns 12
# f(20576,True) returns 8
# f(13115,True) returns 0

import sumofdigits
    
number = 3124
even = True
sum = sumofdigits.f(number, even)
print(f"f({number}, {even}) returns {sum}") 

number = 3124
even = False
sum = sumofdigits.f(number, even)
print(f"f({number}, {even}) returns {sum}") 

number = 20576
even = False
sum = sumofdigits.f(number, even)
print(f"f({number}, {even}) returns {sum}") 

number = 20576
even = True
sum = sumofdigits.f(number, even)
print(f"f({number}, {even}) returns {sum}") 

number = 13115
even = True
sum = sumofdigits.f(number, even)
print(f"f({number}, {even}) returns {sum}") 