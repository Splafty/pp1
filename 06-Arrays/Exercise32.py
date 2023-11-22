# 32.	Define a function occurs(number, array) that returns True if a given number is present in an array. Then create a program that checks whether the number entered from the keyboard is present in the array [15, 38, 7, 23, 14]. 
# Sample result:
# Number: 23
# Array: 15 38 7 23 14
# Result: number 23 appears in the array

def occurs(number, array):
    for element in array:
        if element == number:
            return True
    return False

arr = [15, 38, 7, 23, 14]

number = int(input("Number: "))

print(occurs(number,arr))