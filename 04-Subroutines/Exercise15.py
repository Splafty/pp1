# 15.	Define a function phone_keyboard() that displays numbers in the layout as below (like on a phone keypad).
# Apply a loop statement. Then, call the function. Sample result:

def phone_keyboard():
    for i in range(1,9,3):
        for j in range(3):
            print(f" {i+j}",end=" ")
        print()

phone_keyboard()

