# 10.	Find any text file on the Internet and download it to your computer.
# Then, write a program that displays its content.

file = open('Peter_Pan.txt','r')
file_content = file.read()
print(file_content)
file.close()