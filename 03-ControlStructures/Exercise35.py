output = ""
for i in range (1, 31):
    if i % 5 == 0 and i % 3 == 0:
        output += "BINGO "
    elif i % 5 == 0:
        output += "FIVE "
    elif i % 3 == 0:
        output +="THREE "
    else:
        output += (f"{i}" + " ")

print(f"{output}")