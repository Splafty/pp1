# 44.	A valid password should consist of at least six different characters. 
# Define a function f(password) that returns True if the password is correct or False otherwise. 
# Sample result:
# f("ax15") returns False
# f("book123") returns False
# f("A2water3") returns True
# f("qwerty") returns True
# f("") returns False

import passwordcheck

password = "ax15"
is_correct = passwordcheck.f(password)
print(f"f(\"{password}\") returns \"{is_correct}\"")

password = "book123"
is_correct = passwordcheck.f(password)
print(f"f(\"{password}\") returns \"{is_correct}\"")

password = "A2water3"
is_correct = passwordcheck.f(password)
print(f"f(\"{password}\") returns \"{is_correct}\"")

password = "qwerty"
is_correct = passwordcheck.f(password)
print(f"f(\"{password}\") returns \"{is_correct}\"")

password = ""
is_correct = passwordcheck.f(password)
print(f"f(\"{password}\") returns \"{is_correct}\"")