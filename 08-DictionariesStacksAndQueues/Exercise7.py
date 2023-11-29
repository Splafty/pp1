# 7.	Create a dictionary as in the example below. Note the structure of the dictionary (key-value) and the value types in the example below. What type of value was used in each of the six key-value pairs?

person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

# Then, create a program that:
# a.	Displays contents of the dictionary
print(person.items())
# b.	Displays name
print(person["name"])
# c.	Displays hobby
print(person["hobby"])
# d.	Changes surname to 'Nowak'
person["surname"] = "Nowak"
# e.	Changes person's marriage status
person["married"] = not person["married"]
# f.	Adds gender: 'male'
person["gender"] = "male"
# g.	Adds a new hobby: 'bicycle'
person["hobby"].append("bicycle")
# person["hobby"] = person["hobby"] + ["bicycle"]
# h.	Adds work phone to existing phones: '313131444'
person["phone"]["work"] = "313131444"

print(person.items())