# 22.	The following functions are necessary to handle the stack: push(), pop() and empty(). 
# Below is a simple implementation of the stack using a Python list. 
# Note the definition of the listed functions. 
# What actions do these functions perform? 
# Copy and paste the program code below into a module named stack.py.

#####
# Stack definition
##

stack = []

# add value at the top of the stack
def push(value):
    stack.append(value)
    
# remove the topmost element of the stack
# and return its value    
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
# return true if the stack is empty
def empty():
    return len(stack) == 0

# display stack
def display():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
    print()
