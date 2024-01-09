# 14.	A dictionary contains course names along with the number of hours. 
# Write a program that calculates and displays the total number of hours. 


winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

def f(dictionary):
    hours = sum(dictionary.values())
    return hours

print(f(winter_semester))
