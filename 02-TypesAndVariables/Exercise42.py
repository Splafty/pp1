number = input("Eneter number: ")
decimal_number = 0
for i in range(4):
    decimal_number += int(number[3-i])*(2**i)

print(f"Binary number in deciaml notation: {decimal_number}")