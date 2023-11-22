# 18.	Find any text file on the Internet and download it to your computer.
# Then write a program that copies the contents of this file to the copy.txt file. 
# Copy the contents of the file as a whole. 
# Finally, open both files in any text editor and check that their contents are the same.

with open("Peter_Pan.txt", "r") as f1:
    with open("copy.txt", "w") as f2:
        file_content = f1.read()
        f2.write(file_content)
        
