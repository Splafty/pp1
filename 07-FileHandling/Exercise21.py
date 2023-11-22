# 21.	Create a program that writes to a text file integer numbers in the range <1,50>, every number in a separate line.

with open("numbersinrange.txt", "w") as f1:
    for i in range(1, 51):
        f1.write(f"{i}\n")