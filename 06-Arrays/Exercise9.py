# 9.	An array contains values: 2, 3, 7, 5, 4. 
# Create a program that displays:
arr = [2,3,7,5,4]
# a.	the array
print("Array:",arr)
# b.	number of elements
print("No. of elements:",len(arr))
# c.	first value
print("irst value:",arr[0])
# d.	second value
print("Second value:",arr[1])
# e.	last value
print("Last value:",arr[-1])
# f.	last but one value (do not use negative index values)
print("Last but one value:",arr[len(arr)-2])
# g.	sum of the first and last value
print("Sum of the first and last value:",arr[0]+arr[-1])
# h.	middle value
print("Middle value:",arr[len(arr)//2])
# i.	all array values separated by a single space (use a loop statement)
arr_string = ""
for element in arr:
    arr_string += f"{element} "
print("All array values separated by a single space:",arr_string)