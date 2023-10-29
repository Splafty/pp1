# 24.	In a separate module, define a function that checks if the number is within the range <x, y>. 
# The function returns a boolean value. Then, create a program and use the function you defined. 
# Sample result:
# A number: 7
# Number 7 in the range <2,15>: yes 

import rangecheck

x = 2
y = 15
z = 7

if rangecheck.is_in_range(x,y,z):
    in_range = "yes"
else:
    in_range = "no"

print(f"A number: {z}")
print(f"Number {z} in the range <{x},{y}>: {in_range} ")