# 10.	Find any JSON file on the Internet and download it to your computer. 
# Open the file in any character editor and read its contents. 
# Then, write a program that displays the contents of the JSON file. 
# Sample result:

import json

with open("data.json") as file:
    data = json.load(file)

i = 0
while i < len(data):
    partOfData = data[i]
    print(f"{partOfData['name']}\n{partOfData['surname']}\n{partOfData['gender']}\n{partOfData['age']}\n{partOfData['country']}\n{partOfData['contact']}\n{partOfData['languages']} \n {partOfData['studies']}\n")
    i += 1