# 29.	The grades.txt file contains student’s grades. Create the file in any text editor with the content as below:
# Name: Peter
# Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
# Then, create a program that calculates the arithmetic mean of student’s grades.

import re

with open("grades.txt", "r") as f1:
    text = f1.read()
    sum = 0
    grades = re.findall(r"\d.\d", text)
    for grade in grades:
        sum += float(grade)

    arithmetic_mean = sum/len(grades)
    print(f"{arithmetic_mean:.2f}")