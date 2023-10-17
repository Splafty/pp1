price = float(input("Enter price: "))
discount = int(input("Enter discount %: "))
reduction = price*(discount/100)
price_with_discount = price - reduction 
print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")
