# 38.	A palindrome is an expression that sounds the same when read backwards. 
# Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. 
# Sample result:
# f("radar") returns True
# f("12-11-21") returns True
# f("book") returns False

def f(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False
    

if __name__ == "__main__":
    word = "radar"
    is_a_palindrome = f(word)
    print(f"f({word}) returns {is_a_palindrome}")

    word = "12-11-21"
    is_a_palindrome = f(word)
    print(f"f({word}) returns {is_a_palindrome}")

    word = "book"
    is_a_palindrome = f(word)
    print(f"f({word}) returns {is_a_palindrome}")

