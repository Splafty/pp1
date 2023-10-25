# 12.	Using built-in Python functions, write a program that calculates and displays:


# a.	the largest number given: 7,5,6,3,8,2
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number) 

# b.	binary string representing decimal number 304
number_1 = 304
binary_string = f"{bin(number_1)}"
print(binary_string)

# c.	hexadecimal string representing decimal number 304
number_2 = 304
hexadecimal_string = f"{hex(number_2)}"
print(hexadecimal_string)

# d.	integer representing the Unicode code of the € sign
unicode_sign = "€"
print(f"{ord(unicode_sign)}")

# e.	absolute value of -17
value = -17
print(f"{abs(value)}")
