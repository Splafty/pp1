# 50.	The following function calculates the factorial recursively. 
# Try to analyse the function. Do you understand how it works? 
# Then, write a program and use the function to calculate the factorial value for n = 5.

# def factorial(n):

#     # 0! = 1, 1! = 1
#     if n==0 or n==1:
#         return 1

#     # n! = n * (n-1)!
#     if n > 1:
#         return n * factorial(n-1)


def factorial(n):

    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)
    

if __name__ == "__main__":
    number = 5
    factorialn = factorial(number)
    print(f"f({number}) returns {factorialn}")

    number = 1
    factorialn = factorial(number)
    print(f"f({number}) returns {factorialn}")

    number = 10
    factorialn = factorial(number)
    print(f"f({number}) returns {factorialn}")