# (p6.py) Create a function f(years, course) that, for the data.json file, returns the number of students who are at least the given number of years and have a grade average of at least 4 in the given course name. 
# Example:
# f(21, "statistics") -> compare your result with other students

import json

def f(years, course):
    file = open("data.json", "r")
    data  = json.load(file)
    count = 0
    for student in data:
        if (student["age"] >= years):
            for courses in student["studies"]["courses"]:
                if (courses["name"]) == course:
                    if sum(courses["grades"]) / len(courses["grades"]) >= 4:
                        count += 1
    file.close()

    return count


if __name__ == "__main__":
    print(f(21, "statistics"))