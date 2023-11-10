# (p5.py) The binary system uses two symbols to represent a number: 0 and 1.
# Define a function f(binary_number) that returns True if the given notation is a valid binary number, or false otherwise. 
# Example:
# f("101101") returns True
# f("1311a10100") returns False

def f(binary_number):
    for letter in binary_number:
        if letter != "1" and letter != "0":
            return False
    return True

if __name__ == "__main__":
    bin_number = "101101"
    result = f(bin_number)
    print(f"f({bin_number}) returns {result}")

    bin_number = "1311a10100"
    result = f(bin_number)
    print(f"f({bin_number}) returns {result}")