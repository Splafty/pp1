# 31.	Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. 
# Sample result:
# f(-7,8) returns 3
# f(-1,11) returns 0

def f(x,y):
    num = 0
    if y >= 0:
        while x < 0:
            if x % 2 == 0:
                num += 1
                x += 1
            else:
                x += 1
    else:
        while x <= y:
            if x % 2 == 0:
                num += 1
                x += 1
            else:
                x += 1
    return num

                
if __name__ == "__main__":
    x = -7
    y = 8
    sum = f(x,y)
    print(f"f({x}, {y}) returns {sum}")

    x = -1
    y = 11
    sum = f(x,y)
    print(f"f({x}, {y}) returns {sum}")
