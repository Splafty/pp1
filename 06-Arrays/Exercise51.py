# 51.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last row. 
# Display array values in rows and columns before and after changes.


def swap_rows(array, row1, row2):
    array[row1], array[row2] = array[row2], array[row1]

array_3x5 = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15]]

print("Array before changes:")
print(array_3x5)

swap_rows(array_3x5, 0, 2)

print("\nArray after swapping the first and last rows:")
print(array_3x5)