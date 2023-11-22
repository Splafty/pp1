# 53.	In mathematics, a matrix is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns, e.g.:
# -7  12 38
# 41 -19 11
# Create a function identity_matrix(n) that returns an identity matrix (2D array) of size n (https://en.wikipedia.org/wiki/Identity_matrix). Then, create a function that displays a 2D array in rows and columns. 
# Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8. Sample result:
# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0

def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def display_array(array):
    for row in array:
        for element in row:
            print(element, end=" ")
        print()

# Display identity matrices with dimensions 3, 5, and 8
dimensions = [3, 5, 8]

for dimension in dimensions:
    print(f"\nIdentity Matrix with dimension {dimension}:\n")
    matrix = identity_matrix(dimension)
    display_array(matrix)