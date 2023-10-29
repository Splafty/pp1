# 32.	Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise. 
# Sample result:
# f(11,6,-4) returns True
# f(5,4,14) returns False

import arenegatives

n1 = 11
n2 = 6
n3 = -1
is_there_negative = arenegatives.f(n1, n2, n3)
print(f"f({n1}, {n2}, {n3}) returns {is_there_negative}")

n1 = 5
n2 = 4
n3 = 14
is_there_negative = arenegatives.f(n1, n2, n3)
print(f"f({n1}, {n2}, {n3}) returns {is_there_negative}")