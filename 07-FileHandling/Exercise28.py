# 28.	Find any text file on the Internet and download it to your computer. 
# Then, write a program that displays all words with at least six letters from the file.
# Display each word on a separate line. 
# Use regular expressions.

import re

with open("Peter_Pan.txt", "r") as f1:
    text = f1.read()
    long_words = re.findall(r"\b\w{6,}\b",text)

for word in long_words:
    print(word)