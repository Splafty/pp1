# 25.	An array contains values: 15, 8, 31, 47, 2, 19. 
# Create a program that calculates and displays the array and the arithmetic mean of array values. 
# Use the “while” loop statement.

arr = [15, 8, 31, 47, 2, 19]
sum = 0
i = 0

while i < len(arr):
    sum += arr[i]
    i += 1

print(sum/len(arr))