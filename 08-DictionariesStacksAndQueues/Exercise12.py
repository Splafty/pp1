# 12.	Write a program in which you create a dictionary containing student data. 
# Try to describe a student in detail, using different data types that can be used in the dictionary. 
# Then, save the data about student in the file student.json, in a readable form.

import json

student = { 
    "name": "Urbano",
    "surname": "Rossander",
    "gender": "Male",
    "age": 25,
    "country": "Poland",
    "contact": {
        "email": [
            "urossander0@networkadvertising.org",
            "urossander0@businessinsider.com"
        ],
        "phone": "876 895 602"
    },
    "languages": [
        "English",
        "German",
        "Ukrainian"
    ],
    "studies": {
        "semester": 4,
        "field": "Applied Informatics",
        "fulltime": "no"
    }
}


out_file = open("student.json", "w")

json.dump(student, out_file, indent = 6)

out_file.close()