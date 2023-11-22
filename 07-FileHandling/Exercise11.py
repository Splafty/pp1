# 11.	In any text editor, create a file numbers.txt in which save, in five separate lines, five integer numbers. 
# Then, write a program that reads numbers from the numbers.txt file, calculates their sum and displays result. 
# Tip: read the next line from the file and convert it into a numeric value. 
# Sample result:
# Numbers: 11 9 23 7 2
# Sum: 52

file = open('numbers.txt','r')

sum = 0
for line in file:
     sum += int(line)

file.close()

print(sum)