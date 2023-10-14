buying_rates = float(input("Bank buys EUR: "))
selling_rates = float(input("Bank sells EUR: "))
spread = selling_rates-buying_rates
print(f"Spread: {spread:.4f}")