original_decimal_number = int(input("Enter decimal number: "))
decimal_number = original_decimal_number
binary_number = ""

while decimal_number != 0:
    remainder = decimal_number % 2
    binary_number += f"{remainder}"
    decimal_number = decimal_number // 2

binary_number = binary_number[::-1]
print(f"{decimal_number}(10) = {binary_number}(2)")
print(f"Check: {bin(original_decimal_number)}")