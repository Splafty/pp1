# 43.	A variable contains text:
# An apple a day keeps the doctor away
# Create a module MyText, containing:
# a.	A function that returns the number of words in the text
# b.	A function that returns an ordered array of words, from longest to shortest
# c.	A function that returns an alphabetically ordered array of words
# Then, write a program, call the functions and display results. Sample result:
# Text: An apple a day keeps the doctor away
# Number of words: 8
# Words from the longest: doctor,apple,…
# Words ordered alphabetically: a,An,apple,away,…

my_string = "An apple a day keeps the doctor away"

def count_words(text):
    words = text.split()
    return len(words)

def words_longest_to_shortest(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

def words_alphabetical_order(text):
    words = text.split()
    return sorted(words, key=str.lower)

print(count_words(my_string))
print(words_longest_to_shortest(my_string))
print(words_alphabetical_order(my_string))