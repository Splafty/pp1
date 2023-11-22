# 56.	Create a function that convert two-dimensional (2D) array into 1D. 
# Then create a program that displays 1D array for the following 2D arrays.
# a.	2 3
# 1 5 
# b.	5 0 3 7 5
# 9 0 9 1 2
# c.	2 1
# 3 5
# 7 4
# 2 6

def convert_to_1d(arr_2d):
    return [elem for row in arr_2d for elem in row]

def display_2d_array(arr_2d):
    for row in arr_2d:
        print(" ".join(map(str, row)))

def display_1d_array(arr_1d):
    print(" ".join(map(str, arr_1d)))

# Example 2D arrays
array_a = [
    [2, 3],
    [1, 5]
]

array_b = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

array_c = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Convert and display 1D arrays
print("Original 2D Array A:")
display_2d_array(array_a)
print("\n1D Array A:")
display_1d_array(convert_to_1d(array_a))

print("\nOriginal 2D Array B:")
display_2d_array(array_b)
print("\n1D Array B:")
display_1d_array(convert_to_1d(array_b))

print("\nOriginal 2D Array C:")
display_2d_array(array_c)
print("\n1D Array C:")
display_1d_array(convert_to_1d(array_c))