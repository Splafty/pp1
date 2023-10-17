import random

roll = random.randint(1, 6)
is_special = roll == 1 or roll == 6

print(f"Dice rolled: {roll}")
print(f"Special number: {is_special}")