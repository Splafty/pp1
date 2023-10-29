# 30.	Create a function f(number, even) that computes the sum of the digits of a number. 
# When the value of the even parameter is True, the function returns the sum of the even digits. 
# When the value of the even parameter is False, the function returns the sum of the odd digits. 
# Sample result:
# f(3124,True) returns 6
# f(3124,False) returns 4
# f(20576,False) returns 12
# f(20576,True) returns 8
# f(13115,True) returns 0

def f(number, even):
    number_str = str(number)
    sum = 0
    if even:
        for digit in number_str:
            if int(digit) % 2 == 0:
                sum += int(digit)
            else:
                continue
    else:
        for digit in number_str:
            if int(digit) % 2 == 1:
                sum += int(digit)
            else:
                continue
    return sum

if __name__ == "__main__":
    number = 3124
    even = True
    sum = f(number, even)
    print(f"f({number}, {even}) returns {sum}") 

    number = 3124
    even = False
    sum = f(number, even)
    print(f"f({number}, {even}) returns {sum}") 

    number = 20576
    even = False
    sum = f(number, even)
    print(f"f({number}, {even}) returns {sum}") 

    number = 20576
    even = True
    sum = f(number, even)
    print(f"f({number}, {even}) returns {sum}") 

    number = 13115
    even = True
    sum = f(number, even)
    print(f"f({number}, {even}) returns {sum}") 