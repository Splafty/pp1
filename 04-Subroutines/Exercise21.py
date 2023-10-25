# 21.	In the module mymath.py, define the function generate_number() that creates 
# and returns random integer number in the range of <1,9>. Then create a main program, 
# in which, first import modules mymath.py and mykeyboard.py, you created earlier. 
# The program is a simple guessing game. The user enters a one-digit number from the keyboard. 
# The computer then generates a random one-digit number. If the numbers match, the user wins the game. 
# Sample result:
# Enter a number: 7
# Computer number: 7
# You won the game!!

import mymath
import mykeyboard

guessed_number = mykeyboard.read_number()
computer_number = mymath.generate_number()
print(f"Computer number: {computer_number}")

if guessed_number == computer_number:
    print("You won the game!!")
else:
    print("Not this time!")
