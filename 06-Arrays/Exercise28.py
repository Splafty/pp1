# 28.	Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise.  
# Two arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal. 
# Then create a program and try to compare the following arrays: 

def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

# a.	["water","book","sky"]   ["water","book","sky"]
array1 = ["water","book","sky"] 
array2 = ["water","book","sky"]
print(compare(array1, array2))

# b.	[True,False]   [True,False,True]
array1 = [True,False]
array2 = [True,False,True]
print(compare(array1, array2))

# c.	[5,3,1]   [5,3,1]
array1 = [5,3,1]
array2 = [5,3,1]
print(compare(array1, array2))

# d.	[3,2,1]   [3,2]
array1 = [3,2,1]
array2 = [3,2]
print(compare(array1, array2))
