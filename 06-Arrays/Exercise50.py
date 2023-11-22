# 50.	An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]]. 
# Create a program that finds the smallest and largest values in the array and in which row and column they are located. 

arr = [[-38, 19], [5,40],[-7,11],[29,16]]

largest = arr[0][0]
smallest = arr[0][0]
largest_row= 0
largest_column = 0
smallest_row = 0
smallest_column = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] > largest:
            largest = arr[i][j]
            largest_row = i
            largest_column = j
        elif arr[i][j] < smallest:
            smallest = arr[i][j]
            smallest_row = i
            smallest_column = j

print(largest,largest_column,largest_row)
print(smallest,smallest_column,smallest_row)