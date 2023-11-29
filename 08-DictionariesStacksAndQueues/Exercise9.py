# 9.	Create an array with 5 dictionaries, each containing a name and its population. Then, using a ‘while’ loop, display the array contents. Sample result:

countries = [
    {"name":"Poland", "population":38000000},
    {"name": "USA", "population": 330000000},
    {"name": "China", "population": 1400000000},
    {"name": "India", "population": 1300000000},
    {"name": "Brazil", "population": 200000000},
]

i = 0
while i < len(countries):
    country = countries[i]
    print(f"{country['name']} \t {country['population']}")
    i += 1

