# (p2.py) An array contains at least 3 integers. 
# All numbers in the array are equal except one. 
# Create a function f(arr) that returns a number in the arr array that is different from the other numbers. 
# Example:
# f([7,7,7,7,7,5,7,7]) -> 5

def f(arr):
    for i in range(len(arr)):
        if arr[i] != arr[i+1]:
            if i == 0:
                if arr[i] != arr[i+1] and arr[i] != arr[i+2]:
                    return arr[i]
                else:
                    return arr[i+1]
            else:
                return arr[i+1]



if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))
    print(f([5,7,7,7,7,7,7,7]))
    print(f([7,7,7,7,7,7,7,5]))
    print(f([7,5,7,7,7,7,7,7]))
    print(f([7,7,7,7,7,7,5,7]))

        

