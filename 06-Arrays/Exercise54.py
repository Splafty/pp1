# 54.	Create a function transpose_matrix(m) that returns transposed matrix m:
# https://en.wikipedia.org/wiki/Transpose 

def transpose_matrix(m):
    rows, cols = len(m), len(m[0])
    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = m[i][j]

    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)