number = input("Enter phone number: ")
split_number = f"{number[:3]}-{number[3:6]}-{number[6:9]}"
print(f"Phone number: {split_number}")
