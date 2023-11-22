# 26.	An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy. 
# Create a program that displays the longest name (consisting of the largest number of characters). 
# Sample result:
# Names: Genowefa Onufry Celestyna Alojzy Pankracy
# Longest name: Celestyna

arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = ""

for name in arr:
    if len(name) > len(longest_name):
        longest_name = name

print(longest_name)