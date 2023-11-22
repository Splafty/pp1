# 55.	Then, create a program that displays transposed matrices, in rows and columns, for the following matrices.
# a.	1 2 3
# 4 5 6
# 7 8 9
# b.	1 2 3 4 5
# 6 7 8 9 0
# c.	5 6 7 8

def transpose_matrix(m):
    rows, cols = len(m), len(m[0])
    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = m[i][j]

    return transposed


def display_array(array):
    for row in array:
        for element in row:
            print(element, end=" ")
        print()


matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

matrix_b = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]]

matrix_c = [[5, 6, 7, 8]]

display_array(transpose_matrix(matrix_a))

print("\nTransposed Matrix B:")
display_array(transpose_matrix(matrix_b))

print("\nTransposed Matrix C:")
display_array(transpose_matrix(matrix_c))



