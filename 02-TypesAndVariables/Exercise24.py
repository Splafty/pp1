registration = input("Enter vehicle registration number: ")
is_from_krakow = registration.startswith("KR") or registration.startswith("KK")

print("Car from Kraków: ",is_from_krakow)
