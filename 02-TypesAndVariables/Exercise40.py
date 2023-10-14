credit_card_number = input("Enter credit card number: ")
separated_credit_card_number = f"{credit_card_number[0:4]} {credit_card_number[4:8]} {credit_card_number[8:12]} {credit_card_number[12:16]}" 
print(f"Card number: {separated_credit_card_number}")
