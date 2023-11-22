# 29.	Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
# Create a program that displays the numbers from the first array that do not appear in the second array.

array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]

result = [num for num in array1 if num not in array2]
print(result)