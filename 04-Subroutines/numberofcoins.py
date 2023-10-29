# 29.	The vending machine accepts 1, 2 and 5 PLN coins. 
# Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. 
# Sample result:
# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0

def f(amount_to_pay):
    coin_5 = amount_to_pay // 5
    coin_2 = amount_to_pay % 5 // 2
    coin_1 = amount_to_pay % 5 % 2
    min_num_of_coins = coin_5 + coin_2 + coin_1
    return min_num_of_coins

if __name__ == "__main__":
    amount_to_pay = 23
    min_num_of_coins = f(amount_to_pay)
    print(f"f({amount_to_pay}) returns {min_num_of_coins}")