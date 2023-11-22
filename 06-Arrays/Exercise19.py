# 19.	Try to create the following arrays. 
# Then, display the created array content.

import random

# a.	arr1 = [3,7,1,0,4]
arr1 = [3,7,1,0,4]
print(arr1)

# b.	arr2 = [[2,3],[7,1],[0,4]]
arr2 = [[2,3],[7,1],[0,4]]
print(arr2)

# c.	arr3 = [7 for i in range(5)]
arr3 = [7 for i in range(5)]
print(arr3)

# d.	arr4 = [i for i in range(1,10)]
arr4 = [i for i in range(1,10)]
print(arr4)

# e.	arr5 = [i*2 for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
print(arr5)

# f.	arr6 = [random.randint(1,20) for i in range(10)]
arr6 = [random.randint(1,20) for i in range(10)]
print(arr6)

# g.	arr7 = [[] for i in range(5)]
arr7 = [[] for i in range(5)]
print(arr7)

# h.	arr8 = [[1 for i in range(2)] for j in range(4)]
arr8 = [[1 for i in range(2)] for j in range(4)]
print(arr8)

# i.	arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
print(arr9)

# j.	an array with values: 4,0,3
arr10 = [4,0,3]
print(arr10)

# k.	15-element array filled with zeros
arr11 = [0 for i in range(15)]
print(arr11)

# l.	an array with integer values in the range of <1,30>
arr12 = [i for i in range(1, 31)]
print(arr12)

# m.	20-element array filled with 0 or 1 randomly
arr13 = [random.randint(0,1) for i in range(20)]
print(arr13)

# n.	two dimensional array with five rows and two columns filled with False
arr14 = [[False for i in range(2)] for j in range(5)]
print(arr14)
