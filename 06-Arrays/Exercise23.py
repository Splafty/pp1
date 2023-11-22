# 23.	An array contains numbers: -15, 8, -31, 47, -2, 19. 
# Create a program that finds and displays the maximum and minimum number. 
# Do not use available functions.

arr = [-15, 8, -31, 47, -2, 19]

max_number = arr[1]
min_number = arr[0]
for element in arr:
    if element > max_number:
        max_number = element
    elif element < min_number:
        min_number = element

print(max_number)
print(min_number)