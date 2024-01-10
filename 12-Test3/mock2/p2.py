# (p2.py) Create a function f(x,y,d) that returns true when the string of digits d appears in any number between x and y. 
# Otherwise, the function returns false.
# Example:
# f(10,15,"14")  True
# f(100,120,"11")  True
# f(205,210,"04")  False

def f(x, y, d):
    for num in range(x, y + 1):
        if d in str(num):
            return True
    return False


if __name__ == "__main__":
    print(f(10, 15, "14"))
    print(f(100, 120, "11"))
    print(f(205, 210, "04"))
