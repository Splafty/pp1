# (p5.py) Create a function f(first_letter,last_letter) that, for the data.txt file, returns the number of words that start with the first_letter and end with the last_letter. 
# Example:
# f("w","d") -> compare your result with other students 

import re

def f(first_letter, last_letter):
    file = open("data.txt", "r", encoding="utf-8")
    data = file.read()
    # words = data.split()
    list_of_words=re.findall(fr'\b{first_letter}\w+{last_letter}\b', data)
    # count = 0
    # for word in words:
    #     if (word.lower()).startswith(first_letter) and (word.lower()).endswith(last_letter):
    #         print(word)
    #         count += 1
    # file.close()
    # return count
    return len(list_of_words)

if __name__ == "__main__":
    print(f("w", "d"))