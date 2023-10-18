number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
if number1 > 0 or number2 > 0:
    print(f"At least one of entered numbers {number1} and {number2} is not negative")
else:
    print(f"Both numbers {number1} and {number2} are negative ")