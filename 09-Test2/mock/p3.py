# (p3.py) A two-dimensional array contains the same number of rows and columns. 
# Create a function f(array2D) that, for the given two-dimensional array array2D, returns True when the sum of the values in each row of the array is equal to the sum of the values in the corresponding column (e.g., the sum of the values in row 3 is equal to the sum of the values in column 3) , and False otherwise.
# Example:
# f([[3,7,2],[4,2,5],[5,2,1]]) -> True
# f([[3,7,2],[4,2,5],[9,2,1]]) -> False

def f(arr2D):
    sum_of_row = 0
    sum_of_column = 0
    for i in range (len(arr2D)):
        for j in range(len(arr2D[0])):
            sum_of_row += arr2D[i][j]
            sum_of_column += arr2D[j][i]
        if sum_of_row != sum_of_column:
            return False
        else:
            sum_of_row = 0
            sum_of_column = 0
    return True



if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))