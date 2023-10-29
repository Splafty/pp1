# 33.	Define a function f(n) that returns a string of n asterisks, separated by a slash sign. 
# Sample result:
# f(4) returns "*/*/*/*"
# f(1) returns "*"

import stringofasterisks

n = 4
string_of_asterisks = stringofasterisks.f(n)
print(f"f({n}) returns {string_of_asterisks}")

n = 1
string_of_asterisks = stringofasterisks.f(n)
print(f"f({n}) returns {string_of_asterisks}")