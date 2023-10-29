# 24.	In a separate module, define a function that checks if the number is within the range <x, y>. 
# The function returns a boolean value. Then, create a program and use the function you defined. 
# Sample result:
# A number: 7
# Number 7 in the range <2,15>: yes 

def is_in_range(x,y,z):
    if x <= z and z <= y:
        return True
    else:
        return False