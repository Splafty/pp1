washing_product = "shoes"
rinse = True
spin = False
total_time = 0

if rinse:
    total_time += 15
if spin:
    total_time += 9

if washing_product == "jakcet":
    total_time += 40
elif washing_product == "underwear":
    total_time += 70
elif washing_product == "shoes":
    total_time += 20
else:
    print("Wrong product")


print(f"Total washing time: {total_time} minutes")


