# 15.	The following program displays the contents of a file, line by line:
# f = open("filename.txt")
# for line in f:
#      print(line, end="")
# f.close()
# Rewrite the program using the "with ..." statement. 
# Then, check that the program works properly.

with open("Peter_Pan.txt") as f:
    for line in f:
        print(line, end="")