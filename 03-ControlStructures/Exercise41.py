PIN = "0805"
i = 0

while i < 3:
    entered_PIN = input("Enter the PIN code: ")
    if entered_PIN == PIN:
        print("Correct PIN!")
        break
    else:
        print("Incorrect...")
        i += 1

if i == 3:
    print("Sorry, your payment card has been blocked.")
