# 31.	Create a program that displays all unique elements in an array. 
# Sample result:
# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

arr = [2, 3, 2, 5, 8, 1, 9, 8]

count = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count == 1:
        print(arr[i], end=" ")
    count = 0
    
# Alternative
# unique_elements = list(set(array))
# print("\nUnique elements:", end=" ")
# for num in unique_elements:
#     print(num, end=" ")