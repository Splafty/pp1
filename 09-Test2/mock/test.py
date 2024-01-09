def calculate_rpn(expression):
    stack = []

    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # If the token is a number, push it onto the stack
            stack.append(float(token))
        elif token in "+-*/":
            # If the token is an operator, pop two items from the stack,
            # do the calculation, and push the result back onto the stack
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    # The final result is at the top of the stack
    return stack[0]

if __name__ == "__main__":
    expressions = [
        "2 3 + =",           # 2 + 3
        "2 4 1 + * =",       # 2 * (4 + 1)
        "2 3 + 4 5 + * =",   # (2 + 3) * (4 + 5)
        "8 3 1 + / 3 2 - 4 + * =",  # 8 / (3 + 1) * (3 - 2 + 4)
    ]

    for exp in expressions:
        result = calculate_rpn(exp)
        print(f"Expression: {exp}\nResult: {result}\n")