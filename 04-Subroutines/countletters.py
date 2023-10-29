# 23.	Create a program that calculates how many times the given letter appears in any text. 
# Then create a program and check how many times the letter ‘e’ appears in the text below.
# In a separate module, define a function for making calculations. 
# Sample result:
# You never get a second chance to make a first impression
# The number of letter 'e': 7


def count_letters(text, letter):
    return text.count(letter)


if __name__ == "__main__":
    text = "You never get a second chance to make a first impression"
    letter = "e"
    count = count_letters(text, letter)
    print(f"The number of letter \"{letter}\": {count}")