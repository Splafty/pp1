# 9.	Create a program that displays the contents of the countries.txt text file. 
# At the beginning of each line, display the line number. 
# Tip: read and display text file line by line. 
# Sample result:
# 1. Poland
# 2. Germany
# 3. Slovakia
# 4. Ukraine


# open file
file = open('countries.txt', 'r')

# display text file, line by line
counter = 0
for line in file:
     counter += 1
     print(f"{counter}. {line}", end="")

# close file
file.close()