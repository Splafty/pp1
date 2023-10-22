# 44.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. Entering 0 ends entering numbers. Sample result:
# Enter number: 15
# Enter number: 8
# Enter number: 10
# Enter number: 0
# RESULT: Quantity=3, Sum=33, Mean=11

entered_number = ""
quantity = 0
sum = 0

while True:
    entered_number = float(input("Enter number: "))

    if entered_number == 0:
        break
    else:
        quantity += 1
        sum += entered_number
    
if quantity > 0:
    mean = sum / quantity
else:
    mean = 0

print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")