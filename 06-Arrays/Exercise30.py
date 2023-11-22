# 30.	Create a program that sorts elements of an array containing integer numbers. 
# Apply the Bubble Sort sorting algorithm.
# Define a function bubblesort(array) that returns the sorted array. 
# Try to sort and display any three arrays.

# Python program for implementation of Bubble Sort
 
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return
 
 
#Test
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i], end=" ")

print()

arr = [1, 34, 4, 12, 2, 11, 33]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i], end=" ")

print()

arr = [64, 13, 25, 12, 9, 11, 2]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i], end=" ")