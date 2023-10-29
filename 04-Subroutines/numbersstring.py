# 34.	Define the function f(n), which returns numbers from 1 to n as a string. 
# Sample result:
# f(11) returns "1234567891011"
# f(4) returns "1234"

def f(n):
    i = 1
    numbers_string = ""
    while i <= n:
        numbers_string += f"{i}"
        i += 1
    return numbers_string

if __name__ == "__main__":
    n = 11
    numbers_string = f(n)
    print(f"f({n}) returns {numbers_string}")

    n = 4
    numbers_string = f(n)
    print(f"f({n}) returns {numbers_string}")
