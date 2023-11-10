# (p3.py) A text contains any name of words. 
# Define a function f(name) that returns the acronym (first letters of all words). 
# Sample result:
# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"

def f(name):
    names = name.split(" ")
    acronym = ""
    i = 0
    while i < len(names):
        acronym += names[i][0]
        i += 1
    return acronym


if __name__ == "__main__":
    name = "Internet of Things"
    result = f(name)
    print(f"f({name}) returns {result}")

    name = "For Your Information"
    result = f(name)
    print(f"f({name}) returns {result}")

    name = "Python"
    result = f(name)
    print(f"f({name}) returns {result}")