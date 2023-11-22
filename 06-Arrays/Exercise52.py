# 52.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last column. 
# Display array values in rows and columns before and after changes.


def swap_columns(array, col1, col2):
    for row in array:
        row[col1], row[col2] = row[col2], row[col1]

array_3x5 = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15]]

print("Array before changes:")
print(array_3x5)

swap_columns(array_3x5, 0, 4)

print("\nArray after swapping the first and last columns:")
print(array_3x5)