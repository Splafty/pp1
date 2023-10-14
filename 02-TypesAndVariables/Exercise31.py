import random

roll = random.randint(1, 6)
guess = int(input("Guess the number form 1 to 6: "))
is_guessed = roll == guess
print(is_guessed)