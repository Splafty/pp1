# Wpisujesz ciąg znaków i po każdym ma być + później - + itd

alphabet = "abcdefghijklmnoprstuwxyz"

def f(alphabet):
    i = 1
    final_string = ""
    for letter in alphabet:
        if i % 2 == 1:
            final_string += letter + "+"
            i += 1
        elif i % 2 == 0:
            final_string += letter + "-"
            i += 1
    return final_string[:-1]

print(f(alphabet))