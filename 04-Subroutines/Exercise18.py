# 18.	Define a function numbers(n) that returns a string containing integer numbers from 1 to n,
#  separated by a single space character. Then, call the function and display numbers from 1 to
#   15 and from 1 to 7. Sample result:

def numbers(n):
    i = 1
    num_string = ""
    while i <= n:
        num_string += f"{i}" + " "
        i += 1
    return num_string


n = 15
print(f"Numbers <1, {n}>: {numbers(n)}")

n = 7
print(f"Numbers <1, {n}>: {numbers(n)}")

