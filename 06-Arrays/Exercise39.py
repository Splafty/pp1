# 39.	Write a program to separate even and odd numbers of a given array of integers. Put all even numbers first, and then odd numbers.

arr = [11,12,13,14,1,2,3,4,5,6,7,8,9,10]
arr.sort()
arr2 = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr2.append(arr[i])
        
for i in range(len(arr)):
    if arr[i] % 2 == 1:
        arr2.append(arr[i])

print(arr2)