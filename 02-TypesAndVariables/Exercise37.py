personal_data = "Mr. John May, born on 1998-02-16"
original_personal_data = personal_data
personal_data = personal_data.replace("Mr. ", "")
personal_data = personal_data.replace("born on ", "")
personal_data = personal_data.replace(",", "")
parts = personal_data.split(" ")

name = parts[0]
surname = parts[1]
initials =  parts[0][0] + parts[1][0]
date_of_birth =  parts[2]

print(f"Description: {original_personal_data}")
print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Initials: {initials}")
print(f"Born: {date_of_birth}")
