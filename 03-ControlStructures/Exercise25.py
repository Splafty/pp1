number_of_products = int(input("Number of products purchased: "))
product_price = int(input("Product price: "))
amount_to_pay = 0
i = 1
while i <= number_of_products:
    if i <= 2:
        amount_to_pay += product_price
        i += 1
    else:
        amount_to_pay += product_price * 0.75
        i += 1
print(f"Amount to pay: {amount_to_pay}")
