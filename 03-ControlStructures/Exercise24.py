current_product_price = 140.00
previous_product_price = 200.00
discount = 100 - (current_product_price / previous_product_price * 100)
if discount >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {discount}%")
