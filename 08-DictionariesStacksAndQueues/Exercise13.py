# 13.	A program contains any defined dictionary, with any number of key-value pairs of information.
# Write a program that displays the number of pairs of information available in the dictionary.

def count_dict_pairs(my_dict):
    num_pairs = len(my_dict)
    return num_pairs

my_dictionary = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'occupation': 'Engineer'
}

pairs_count = count_dict_pairs(my_dictionary)

print(f'The number of key-value pairs in the dictionary is: {pairs_count}')
