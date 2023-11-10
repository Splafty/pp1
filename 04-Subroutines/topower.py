# 52.	Define a function power(x, n) that calculates xn. 
# Apply recursion. 
# Then, calculate 53.
# Tip: x^n =  x * x^(n-1)

def power(x, n):
    # 0! = 1, 1! = 1
    if n==0:
        return 1
    elif n==1:
        return x
    # n! = n * (n-1)!
    if n > 1:
        return x * power(x, n-1)
    

if __name__ == "__main__":
    x = 5
    n = 3
    result = power(x, n)
    print(f"f({x, n}) returns {result}")

    x = 4
    n = 0
    result = power(x, n)
    print(f"f({x, n}) returns {result}")

    x = 2
    n = 4
    result = power(x, n)
    print(f"f({x, n}) returns {result}")