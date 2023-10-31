# 39.	A sentence is an ordered group of wor ds separated by spaces (spaces). 
# Define a function f(sentence) that returns a sentence with spaces removed. 
# Sample result:
# f("integrated development environment") returns "integrateddevelopmentenvironment"
# f("A programming language is a system of notation for writing computer programs") returns "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms" 

import spaceremover

sentence = "integrated development environment"
stripped_sentence = spaceremover.f(sentence)
print(f"f(\"{sentence}\") returns \"{stripped_sentence}\"")

sentence = "A programming language is a system of notation for writing computer programs"
stripped_sentence = spaceremover.f(sentence)
print(f"f(\"{sentence}\") returns \"{stripped_sentence}\"")
