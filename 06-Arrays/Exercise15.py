# 15.	An array contains values: [[1,3,5],[8,7,2]]. 
# Write a program that calculates and displays:
# Sample result:
# 3
# 10
# 17

arr = [[1,3,5],
       [8,7,2]]

# a.	Sum of the first element in the first row and the last element in the last row
print(arr[0][0] + arr[-1][-1])
# b.	Sum of the elements in the middle column
print(arr[0][1] + arr[1][1])
# c.	Sum of the elements in the last row
sum = 0
for element in arr[1]:
    sum += element

print(sum)


