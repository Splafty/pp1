# 24.	An array contains values: 15, 8, 31, 47, 2, 19.
# Create a program that calculates and displays the array and the arithmetic mean of array values. 
# Use the “for” loop statement.

arr = [15, 8, 31, 47, 2, 19]
sum = 0
for element in arr:
    sum += element

print(sum/len(arr))