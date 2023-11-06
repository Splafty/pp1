# 45.	An expression contains operators for adding and subtracting single-digit numbers. 
# Define a function f(expression) that returns the value of the expression. 
# Sample result:
# f("2+3") returns 5
# f("3+8+1") returns 12
# f("2+3-4+5-0") returns 6

import expressionvalue

expression = "2+3"
value = expressionvalue.f(expression)
print(f"f({expression}) returns {value}")

expression = "3+8+1"
value = expressionvalue.f(expression)
print(f"f({expression}) returns {value}")

expression = "2+3-4+5-0"
value = expressionvalue.f(expression)
print(f"f({expression}) returns {value}")