# 28.	The binary numerical system uses two symbols to represent a number: 0 and 1. 
# Define a function f(binary_number_1) that returns True if the given string of digits is a valid binary number, or False otherwise. 
# Sample result:
# f("101101") returns True
# f("1311a10100") returns False

import isbinary

binary_number_1 = "101101"
is_binary_1 = isbinary.f(binary_number_1)
print(f"(\"{binary_number_1}\") returns \"{is_binary_1}\"")

binary_number_2 = "1311a10100"
is_binary_2 = isbinary.f(binary_number_2)
print(f"(\"{binary_number_2}\") returns \"{is_binary_2}\"")