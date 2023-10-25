# 19.	In a separate module, define a function that calculates the sum of digits. 
# Use the function to calculate the sum of digits entered from the keyboard. 
# To do it, copy the following modules. Then, run the programs digits.py and myprogram.py separately. 
# Try to analyze the results. Do you understand how to import a module and how to call the functions 
# contained in the module?


def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == "__main__":
    # check if function works
    print(sum_digits(7182))
    print(sum_digits(0))
    print(sum_digits(333))

