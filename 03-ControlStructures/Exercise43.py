# 43.	Write a program that displays the first twenty words of the Fibonacci sequence. 
# The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two. Sample result: 
# https://en.wikipedia.org/wiki/Fibonacci_number
# 0 1 1 2 3 5 8 13 21 34 ...

i = 0
j = 1
k = 0

print(i, j, end=" ")

for num in range (1,19):
    k = i + j
    print(f"{k}", end=" ")
    i = j
    j = k