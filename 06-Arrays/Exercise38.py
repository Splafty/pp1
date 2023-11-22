# 38.	Write a program that, for the given array of real numbers, displays the number of elements that are greater than the given value entered from the keyboard.

arr = [11,12,13,14,1,2,3,4,5,6,7,8,9]

value = int(input("Enter a number: "))

arr.sort()
count = 0

for element in arr:
    if element > value:
        count += 1

print(count)