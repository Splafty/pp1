# 16.	A program contains two functions:
# a.	hotel_list(hotels) that returns a list of hotels names, separated by a comma sign
# b.	avg_price(hotels) that returns the average room price for a given list of hotels, rounded to an integer value
# c.	Write a program that calculates and displays the average price for a room in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper.

def hotel_list(hotels):
    hotels_string = ""
    for hotel in hotels:
        hotels_string += hotel["name"] + ","
    return hotels_string[:-1]

def avg_price(hotels):
    sum = 0
    for hotel in hotels:
        sum += hotel["price"]
    return round(sum / len(hotels))

Hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]

print("Hotels in Krakow:", hotel_list(Hotels_in_Krakow))
print("Average hotel price in Krakow:", avg_price(Hotels_in_Krakow))

print("\nHotels in Sopot:", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot:", avg_price(hotels_in_Sopot))

krakow_avg_price = avg_price(Hotels_in_Krakow)
sopot_avg_price = avg_price(hotels_in_Sopot)

if krakow_avg_price < sopot_avg_price:
    cheaper_city = "Krakow"
elif krakow_avg_price > sopot_avg_price:
    cheaper_city = "Sopot"
else:
    cheaper_city = "Both cities"

print("Cheaper hotels in:", cheaper_city)
