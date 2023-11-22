# 8.	In any text editor, create a text file countries.txt in which save, in five separate lines, names of five countries. 
# Then, write a program that displays file content. 
# Sample result:
# Poland
# Germany
# Slovakia
# Ukraine
# Lithuania

file = open('countries.txt','r')
file_content = file.read()
print(file_content)
file.close()