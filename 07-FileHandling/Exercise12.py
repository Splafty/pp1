# 12.	Create a program that saves in the student.txt file, in three separate lines, your name and surname, university name and field of study.  
# Tip: open a file in writing mode and use the write() method. 

# define personal data
name = "Anna May"
university = "Krakow University of Economics"
field = "Applied Informatics"

# write to a file
file = open("student.txt", 'w')
file.write(name+"\n")
file.write(university+"\n")
file.write(field+"\n")
file.close()
