# 20.	An array contains integer numbers: 34,7,19,4,21,8. 
# Create a program that calculates and displays the number of even values in the array. 
# Use the ‘while’ loop statement.

arr = [34,7,19,4,21,8]
number = 0
i = 0

while i < len(arr):
    if arr[i] % 2 == 0:
        number += 1
        i += 1
    else:
        i += 1

print(number)