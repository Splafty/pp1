# 16.	Write a program that calculates the number of lines for any text file. 
# The user enters the name of the file from the keyboard. 
# Display the result of the calculation (the file name and the number of lines). 
# Do not display the contents of the file. 
# Sample result:
# File name: countries.txt
# Number of lines: 14

file_name = input("File name: ")

count = 0
with open(f"{file_name}") as f:
    for line in f:
        count +=1
print("Number of lines: ", count)