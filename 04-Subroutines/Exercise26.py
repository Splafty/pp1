# 26.	Define an anonymous function that returns True when a number is even or False otherwise.

is_even = lambda x: True if x % 2 == 0 else False

check_1 = is_even(7)
check_2 = is_even(8)

print(check_1)
print(check_2)