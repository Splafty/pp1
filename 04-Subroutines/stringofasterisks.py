# 33.	Define a function f(n) that returns a string of n asterisks, separated by a slash sign. 
# Sample result:
# f(4) returns "*/*/*/*"
# f(1) returns "*"

def f(n):
    string_of_asterisks = ""
    if n == 1:
        string_of_asterisks = "*"
    elif n > 1:
        string_of_asterisks = "*" + "/*" * (n-1)
    else:
        string_of_asterisks = ""
    return string_of_asterisks

if __name__ == "__main__":
    n = 4
    string_of_asterisks = f(n)
    print(f"f({n}) returns {string_of_asterisks}")

    n = 1
    string_of_asterisks = f(n)
    print(f"f({n}) returns {string_of_asterisks}")


