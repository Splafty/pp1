time_24_format = input("Enter time (24-hour format): ")
time_parts = time_24_format.split(":")
hours = int(time_parts[0])
minutes = int(time_parts[1])

if hours == 0:
    part_of_the_day ="am"
    time_12_format =f"12:{minutes:02d}"
elif hours < 12:
    part_of_the_day = "am"
    time_12_format = f"{hours}:{minutes:02d}"
elif hours == 12:
    part_of_the_day = "pm"
    time_12_format = f"{hours}:{minutes:02d}"
else:
    part_of_the_day = "pm"
    time_12_format = f"{hours-12}:{minutes:02d}"


print(f"Time in 12-hour format: {time_12_format}{part_of_the_day}")