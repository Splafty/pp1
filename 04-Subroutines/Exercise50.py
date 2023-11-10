# 50.	The following function calculates the factorial recursively. 
# Try to analyse the function. Do you understand how it works? 
# Then, write a program and use the function to calculate the factorial value for n = 5.

# def factorial(n):

#     # 0! = 1, 1! = 1
#     if n==0 or n==1:
#         return 1

#     # n! = n * (n-1)!
#     if n > 1:
#         return n * factorial(n-1)

import factorialfunction

number = 5
factorial = factorialfunction.factorial(number)
print(f"f({number}) returns {factorial}")

number = 1
factorial = factorialfunction.factorial(number)
print(f"f({number}) returns {factorial}")

number = 10
factorial = factorialfunction.factorial(number)
print(f"f({number}) returns {factorial}")