# 25.	Define an anonymous function that returns True when the first number is greater than the second one. 
# Otherwise returns False. Use a conditional operator. 
# Then, check the function for pairs of numbers: 34, 25 and 19,23.

is_greater = lambda x,y: True if x > y else False

check_1 = is_greater(34, 25)
check_2 = is_greater(19, 23)

print(check_1)
print(check_2)