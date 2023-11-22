# 22.	Create a program that writes 50 random integers between 100 and 999 to a text file, each number on a separate line.

import random

with open("randomnumbers.txt", "w") as f1:
    for i in range(51):
        number = random.randint(100,999)
        f1.write(f"{number}\n")