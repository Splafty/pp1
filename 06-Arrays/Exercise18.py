# 18.	An array contains values: [[True,False],[True,True],[False,False]]. 
# Create a program that changes values of an array to the opposite. 
# Use a loop statement. 
# Sample result:
# Before: [[True,False],[True,True],[False,False]]
# After:  [[False,True],[False,False],[True,True]]

arr = [[True,False],
       [True,True],
       [False,False]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]:
            arr[i][j] = False
        else:
            arr[i][j] = True
print(arr)