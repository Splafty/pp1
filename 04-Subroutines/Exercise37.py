# 37.	Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
# The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
# Each subsequent value is the sum of the previous two. 
# Sample result:
# f(5) returns 3
# f(9) returns 21

import fibonaccicalculator

n = 5
fibonacci = fibonaccicalculator.f(n)
print(f"f({n}) returns {fibonacci}")

n = 9
fibonacci = fibonaccicalculator.f(n)
print(f"f({n}) returns {fibonacci}")

n = 11
fibonacci = fibonaccicalculator.f(n)
print(f"f({n}) returns {fibonacci}")