# 43.	A text contains any number of words. 
# Define a function f(name) that returns the acronym (first letters of all words). 
# Sample result:
# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"

def f(name):
    words = name.split()
    i = 0
    acronym = ""
    while i < len(words):
        acronym += words[i][0]
        i += 1
    return acronym

if __name__ == "__main__":
    name = "Internet of Things"
    acronym = f(name)
    print(f"f(\"{name}\") returns \"{acronym}\"")

    name = "For Your Information"
    acronym = f(name)
    print(f"f(\"{name}\") returns \"{acronym}\"")

    name = "Python"
    acronym = f(name)
    print(f"f(\"{name}\") returns \"{acronym}\"")