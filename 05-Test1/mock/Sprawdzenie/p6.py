# (p6.py) Create a function f(number, even) that computes the sum of the digits of a number. 
# When the value of the even parameter is True, the function returns the sum of the even digits. 
# When the value of the even parameter is False, the function returns the sum of the odd digits. 
# Example:
# f(3124,True) returns 6
# f(3124,False) returns 4
# f(20576,False) returns 12
# f(20576,True) returns 8
# f(13115,True) returns 0

def f(number, even):
    sum = 0
    number = str(number)

    if even:
        for x in number:
            if int(x) % 2 == 0:
                sum += int(x)
        return sum
    
    if not even:
        for x in number:
            if int(x) % 2 == 1:
                sum += int(x)
        return sum
    

if __name__ == "__main__":
    number = 3124
    even = True
    result = f(number, even)
    print(f"f({number}) returns {result}")

    number = 3124
    even = False
    result = f(number, even)
    print(f"f({number}) returns {result}")

    number = 20576
    even = False
    result = f(number, even)
    print(f"f({number}) returns {result}")

    number = 20576
    even = True
    result = f(number, even)
    print(f"f({number}) returns {result}")

    number = 13115
    even = True
    result = f(number, even)
    print(f"f({number}) returns {result}")