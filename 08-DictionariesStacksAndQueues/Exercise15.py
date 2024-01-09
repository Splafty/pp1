# 15.	The program contains two dictionaries with personal data:

basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

# Write a program that creates a dictionary called ‘person’ containing data from the two given dictionaries (five key-value pairs). 
# Display the contents of the ‘person’ dictionary.

def f(dict1, dict2):
    finaldict = {}
    for key, value in dict1.items():
        finaldict[key] = value
    for key, value in dict2.items():
        finaldict[key] = value
    return finaldict
    

print(f(basic_data, advanced_data))
