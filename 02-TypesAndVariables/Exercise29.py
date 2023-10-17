import random

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
roll3 = random.randint(1, 6)

sum_of_rolls = roll1 + roll2 + roll3

# Display the results
print(f"First dice roll: {roll1}")
print(f"Second dice roll: {roll2}")
print(f"Third dice roll: {roll3}")
print(f"Sum of dice rolled: {sum_of_rolls}")