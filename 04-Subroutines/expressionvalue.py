# 45.	An expression contains operators for adding and subtracting single-digit numbers. 
# Define a function f(expression) that returns the value of the expression. 
# Sample result:
# f("2+3") returns 5
# f("3+8+1") returns 12
# f("2+3-4+5-0") returns 6

def f(expression):
    i = 0
    value = int(expression[0])
    while i < len(expression):
        if expression[i] == "+":
            value += int(expression[i+1])
            i += 1
        elif expression[i] == "-":
            value -= int(expression[i+1])
            i += 1
        else:
            i += 1
    return value

if __name__ == "__main__":
    expression = "2+3"
    value = f(expression)
    print(f"f({expression}) returns {value}")

    expression = "3+8+1"
    value = f(expression)
    print(f"f({expression}) returns {value}")

    expression = "2+3-4+5-0"
    value = f(expression)
    print(f"f({expression}) returns {value}")