# 27.	Write a program that computes the number of words in the following text. 
# Use regular expressions.
# To be, or not to be, that is the question

import re

text = "To be, or not to be, that is the question"

# words = text.split(" ")
# print(len(words))

words = re.split("\s", text)
print(len(words))