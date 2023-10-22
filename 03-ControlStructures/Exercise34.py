amount_of_money = int(input("Enter the amount in PLN: "))
coin_5 = amount_of_money // 5
coin_2 = amount_of_money % 5 // 2
coin_1 = amount_of_money % 5 % 2 

print(f"The amount of PLN {amount_of_money} in coins: ")
print(f"5 zł - {coin_5}")
print(f"2 zł - {coin_2}")
print(f"1 zł - {coin_1}")