# 16.	An array contains values: [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]. 
# Create a program that calculates the sum of all odd numbers. 

arr = [[3,9,2],
       [2,4,5],
       [7,1,6],
       [0,4,8]]

sum_odd = 0
for row in arr:
    for element in row:
        if element % 2 == 1:
            sum_odd += element

print(sum_odd)
