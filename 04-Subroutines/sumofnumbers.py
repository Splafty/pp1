# 40.	Define a function f(number) that returns the sum of repeated digits in a number. 
# Sample result:
# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21 

def f(number):
    # Convert the input number to a string to iterate through its digits
    number_str = str(number)
    
    # Initialize a list with 10 elements, each corresponding to a digit (0 to 9)
    # These elements will store the count of each digit in the input number
    digit_count = [0] * 10

    # Iterate through each digit in the input number
    for digit in number_str:
        digit = int(digit)  # Convert the character to an integer
        digit_count[digit] += 1  # Increment the count for the corresponding digit

    # Calculate the sum of repeated digits by multiplying the digit by its count and summing them
    i = 1
    repeated_digit_sum = 0
    while i < 10:
        if digit_count[i] > 1:
            repeated_digit_sum += digit_count[i] * i
            i += 1
        else:
            i += 1
    return repeated_digit_sum

if __name__ == "__main__":
    number = "1027"
    sum_of_repeated_digits = f(number)
    print(f"f({number}) returns {sum_of_repeated_digits}")

    number = "230335"
    sum_of_repeated_digits = f(number)
    print(f"f({number}) returns {sum_of_repeated_digits}")

    number = "513553007"
    sum_of_repeated_digits = f(number)
    print(f"f({number}) returns {sum_of_repeated_digits}")