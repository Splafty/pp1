# 49.	The sequence of digits contains the number of points rolled with a dice. 
# Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. 
# Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

import diceinarow

dice = "5233165554211"
max_roll = diceinarow.f(dice)
print(f"f({dice}) returns {max_roll}")

dice = "2133"
max_roll = diceinarow.f(dice)
print(f"f({dice}) returns {max_roll}")

dice = "111144444111"
max_roll = diceinarow.f(dice)
print(f"f({dice}) returns {max_roll}")

dice = ""
max_roll = diceinarow.f(dice)
print(f"f({dice}) returns {max_roll}")