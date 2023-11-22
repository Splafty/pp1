# 19.	Find any text file on the Internet and download it to your computer. 
# Then, write a program that copies the contents of this file to the copylines.txt file. 
# Copy the contents of the file line by line. 
# Finally, open both files in any text editor and check that their contents are the same.

with open("Peter_Pan.txt", "r") as f1:
    with open("copylines.txt", "w") as f2:
        for line in f1:
            f2.write(line)
        
        