# 41.	Write a program that checks whether the first array is a subset of the second one (whether all elements of the first array appear in the second array).

arr1 = [3,8,11,2,4,1,1,1,17]
arr2 = [12,13,14,15,1,1,1,2,3,4,5,6,7,8,9,10,11]


def is_subset(arr1, arr2):
    set_arr1 = list(set(arr1))
    set_arr2 = list(set(arr2))
    count = 0

    for i in range(len(set_arr1)):
        for j in range(len(set_arr2)):
            if set_arr1[i] == set_arr2[j]:
                count += 1
    if count == len(set_arr1):
        return True
    else:
        return False
    

print(is_subset(arr1,arr2))

# def is_subset(array1, array2):
#     set1 = set(array1)
#     set2 = set(array2)

#     return set1.issubset(set2)

# # Example usage
# array1 = [1, 2, 3]
# array2 = [1, 2, 3, 4, 5]

# if is_subset(array1, array2):
#     print("Array 1 is a subset of Array 2.")
# else:
#     print("Array 1 is not a subset of Array 2.")