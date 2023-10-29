# 27.	The credit card number consists of 16 digits. 
# In a separate module, define a function f(card_number) that masks the card number. 
# The function returns a character string in which only the first two and the last four digits of the card number are visible.
# The remaining digits of the card number are replaced with an asterisk. Then, create a program that masks some credit card digits. 
# Import the module with the created function. 
# Finally, display the credit card number. Sample result:
# f("5290312400019022") returns "52**********9022"

import masknumber

card_number = "5290312400019022"
masked_number = masknumber.f(card_number)
print(f"(\"{card_number}\") returns \"{masked_number}\"")

