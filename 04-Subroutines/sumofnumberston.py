# 51.	Define a function sum(n) that for the given natural number n calculates the sum of all natural numbers between 1 and n. 
# Apply recursion.5 
# Then, create a program that calculates the sum of natural numbers in the range <1,10>.

def sum(n):
    if n == 1:
        return 1
    
    if n > 1:
        return n + sum(n-1)
    

if __name__ == "__main__":
    number = 5
    sumton = sum(number)
    print(f"f({number}) returns {sumton}")

    number = 1
    sumton = sum(number)
    print(f"f({number}) returns {sumton}")

    number = 10
    sumton = sum(number)
    print(f"f({number}) returns {sumton}")