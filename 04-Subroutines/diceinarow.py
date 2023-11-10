# 49.	The sequence of digits contains the number of points rolled with a dice. 
# Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. 
# Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice):
    if dice == "":
        return None  

    max_roll = None
    max_count = 1
    current_roll = dice[0]
    current_count = 1

    for i in range(1, len(dice)):
        if dice[i] == current_roll:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                max_roll = current_roll
        else:
            current_roll = dice[i]
            current_count = 1

    return max_roll

if __name__ == "__main__":
    dice = "5233165554211"
    max_roll = f(dice)
    print(f"f({dice}) returns {max_roll}")

    dice = "2133"
    max_roll = f(dice)
    print(f"f({dice}) returns {max_roll}")

    dice = "11111444444"
    max_roll = f(dice)
    print(f"f({dice}) returns {max_roll}")

    dice = ""
    max_roll = f(dice)
    print(f"f({dice}) returns {max_roll}")