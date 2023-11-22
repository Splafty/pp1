# 40.	The array contains integer 8 numbers in the range 1 to 999. 
# Write a program that displays elements of the array formatted as below.
# -----------------------------------------
# |   1|  23|   5| 382|   1|  17|   4| 906|
# -----------------------------------------

arr = [1,23,5,382,1,17,4,906]
number_string = "|"

for element in arr:
    if element < 10:
        number_string += f"   {element}|"
    elif element < 100:
        number_string += f"  {element}|"
    elif element < 1000:
        number_string += f" {element}|"


print("-----------------------------------------")
print(number_string)
print("-----------------------------------------")