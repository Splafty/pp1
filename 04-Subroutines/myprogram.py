# 19.	In a separate module, define a function that calculates the sum of digits. 
# Use the function to calculate the sum of digits entered from the keyboard. 
# To do it, copy the following modules. Then, run the programs digits.py and myprogram.py separately. 
# Try to analyze the results. Do you understand how to import a module and how to call the functions 
# contained in the module?


import digits

number = int(input("Enter a number: "))
sum_d = digits.sum_digits(number)
msg = f"Sum of digits {number} is {sum_d}"
print(msg)