# 11.	Create a dictionary that describes your favorite book or movie with at least five key-value pairs. 
# Then, create a program that writes the dictionary data to the favourite.json file. 
# Use the dump() method. 
# Pay attention to the formatting of the data in the json file.
# Use the 'indent' parameter in the dump() method.

import json

movie = {
    "title":"Harry Potter and the Half-Blood Prince",
    "year": 2009,
    "actor":{"leading":"Daniel Radcliffe","supporting":"Emma Watson"},
    "oscar":False,
    "story": "J. K. Rowling"
}


out_file = open("movie.json", "w")

json.dump(movie, out_file, indent = 6)

out_file.close()