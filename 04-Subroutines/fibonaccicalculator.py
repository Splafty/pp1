# 37.	Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
# The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
# Each subsequent value is the sum of the previous two. 
# Sample result:
# f(5) returns 3
# f(9) returns 21

def f(n):
    if n <= 0:
        fibonacci = None
    if n == 1:
        fibonacci = 0
    elif n == 2:
        fibonacci = 1
    else:
        x = 0
        y = 1
        i = 3
        while i <= n:
            fibonacci = x + y
            x = y
            y = fibonacci
            i += 1
    return fibonacci

if __name__ == "__main__":
    n = 5
    fibonacci = f(n)
    print(f"f({n}) returns {fibonacci}")

    n = 9
    fibonacci = f(n)
    print(f"f({n}) returns {fibonacci}")
