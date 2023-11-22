# 37.	Create a module MyArrays containing functions to operate on an array of numbers:
# a.	A function that returns the second largest element in an array

def second_largest(arr):
    largest = arr[0]
    second_largest = arr[0]
    for element in arr:
        if element > largest:
            largest = element
        elif element > second_largest:
            second_largest = element
    return second_largest

# b.	A function that returns the difference between the largest and smallest values in an array

def largest_minus_smallest(arr):
    largest = arr[0]
    smallest = arr[0]
    for element in arr:
        if element > largest:
            largest = element
        elif element < smallest:
            smallest = element
    return largest - smallest

# c.	A function that returns the median of numbers in an array. Do not use built-in functions. The median is the middle value in the ordered sequence of numbers:
# https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png 

def median_of_array(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        median = (arr[len(arr)//2] + arr[len(arr)//2 + 1])/2
    else:
        median = (arr[len(arr)//2])
    return median


# d.	A function that returns a two-element array containing the smallest and largest values in an array

def smallest_and_largest(arr):
    largest = arr[0]
    smallest = arr[0]
    for element in arr:
        if element > largest:
            largest = element
        elif element < smallest:
            smallest = element
    arr2 = [smallest, largest]
    return arr2

# e.	A function that returns array elements as a string, separated by the minus sign

def elements_as_strings(arr):
    string_of_elements = ""
    for i in range (len(arr)):
        string_of_elements += (f"{arr[i]}-")
    return string_of_elements[:-1]

# Then, write a program that for the sequence of numbers:
# 7,3,8,5,2
# calculates and displays results. Sample result:
# Numbers: 7,3,8,5,2
# Second largest number: 7 
# Median: 5
# Smallest and largest number: 2,8
# Numbers as a string: 7-3-8-5-2

if __name__ == "__main__":
    arr = [7,3,8,5,2]
    print(arr)
    print(second_largest(arr))
    print(largest_minus_smallest(arr))
    print(median_of_array(arr))
    print(smallest_and_largest(arr))
    print(elements_as_strings(arr))