# 19.	Using the website https://mockaroo.com, generate a list of 500 students, containing the following data: name, surname, student ID, gender, age, year of study, email. 
# Write the data to the students.json file. 
# Then, write a program that creates the limited.json file containing the list of students limited to data: first name, last name, student id.

import json

file = open("students.json", "r")
data = json.load(file)
limited = []
for student in data:
    limited.append({"first_name": student["name"], "last_name": student["surname"], "student_id": student["student_id"]})
file.close()

with open("limited.json", "w") as file:
    json.dump(limited, file, indent=2)