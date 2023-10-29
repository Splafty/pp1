# 28.	The binary numerical system uses two symbols to represent a number: 0 and 1. 
# Define a function f(binary_number) that returns True if the given string of digits is a valid binary number, or False otherwise. 
# Sample result:
# f("101101") returns True
# f("1311a10100") returns False

def f(binary_number):
    i = 0
    while i < len(binary_number):
        if binary_number[i] == "0" or binary_number[i] == "1":
            i+=1
        else:
            return False
    return True
            
if __name__ == "__main__":
    binary_number = "101101"
    is_binary = f(binary_number)
    print(f"(\"{binary_number}\") returns \"{is_binary}\"")
