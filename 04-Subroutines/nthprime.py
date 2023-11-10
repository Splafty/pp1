# 41.	Define the function f(n) that returns the n-th prime number. 
# A prime number is a natural number greater than 1, divisible by 1 and that number. 
# Sample result:
# f(1) returns 2
# f(5) returns 11

#Function checking if number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

#Function returning nth prime
def f(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            prime = num
            count += 1
        num += 1
    return prime

if __name__ == "__main__":
    n = 1
    n_prime = f(n)
    print(f"f({n}) returns {n_prime}")

    n = 5
    n_prime = f(n)
    print(f"f({n}) returns {n_prime}")
