# 20.	In the module mykeyboard.py, define a function read_number() that returns an integer number
# entered from the keyboard. The function should print a text prompting user to enter data
# 'Enter a number: '. Then, use the function to read two numbers from the keyboard.
# To test the function, use the __name__ variable. Display the sum of two entered numbers. 

def read_number():
    number = int(input("Enter a number: "))
    return number



if __name__ == "__main__":
    # check if function works
    n1 = read_number()
    n2 = read_number()
    print(f"{n1} + {n2} = {n1 + n2}")