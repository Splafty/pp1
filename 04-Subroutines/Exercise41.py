# 41.	Define the function f(n) that returns the n-th prime number. 
# A prime number is a natural number greater than 1, divisible by 1 and that number. 
# Sample result:
# f(1) returns 2
# f(5) returns 11

import nthprime

n = 1
n_prime = nthprime.f(n)
print(f"f({n}) returns {n_prime}")

n = 5
n_prime = nthprime.f(n)
print(f"f({n}) returns {n_prime}")