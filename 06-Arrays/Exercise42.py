# 42.	Define a function rand_elem(array) that returns a randomly selected array element. 
# Using the function, display a few randomly selected array elements.

import random

arr = [12,13,14,15,1,1,1,2,3,4,5,6,7,8,9,10,11]

def rand_elem(array):
    number = random.randint(0, len(array)-1)
    return array[number]

print(rand_elem(arr))