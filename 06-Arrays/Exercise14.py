# 14.	An array contains values: [[2,5,4],[9,0,3]]. 
# Create a program that displays:
# Sample result:
# [[2,5,4],[9,0,3]]
# 2 3
# 5
# 3
# 9 0 3

arr = [[2,5,4],
       [9,0,3]]

# a.	the array
print(arr)
# b.	size of the array (number of rows and columns)
print(len(arr), len(arr[0])) 
# c.	value 5 from the array
print(arr[0][1])
# d.	value 3 from the array
print(arr[1][2])
# e.	second row of the array as below:
arr_string = ""
for i in range (0, 3):
    arr_string += f"{arr[1][i]} "
print(arr_string)
