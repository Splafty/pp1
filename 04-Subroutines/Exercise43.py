# 43.	A text contains any number of words. 
# Define a function f(name) that returns the acronym (first letters of all words). 
# Sample result:
# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"

import floawacronym

name = "Internet of Things"
acronym = floawacronym.f(name)
print(f"f(\"{name}\") returns \"{acronym}\"")

name = "For Your Information"
acronym = floawacronym.f(name)
print(f"f(\"{name}\") returns \"{acronym}\"")

name = "Python"
acronym = floawacronym.f(name)
print(f"f(\"{name}\") returns \"{acronym}\"")