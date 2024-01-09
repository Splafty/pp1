# (p1.py) The playing cards have the following values: Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 10 each. 
# The other cards have the value indicated by the card number. 
# Create a function f(player1,player2) that returns true if the first player has cards of the same or higher value, and false otherwise. 
# Example:
# f("AJ972","AQT72") -> False
# f("9532","K8") -> True

def f(player1, player2):
    sum1 = 0
    sum2 = 0
    for letter in player1:
        if letter.isdigit():
            sum1 += int(letter)
        else:
            sum1 += 10
        
    for letter in player2:
        if letter.isdigit():
            sum2 += int(letter)
        else:
            sum2 += 10
        
    return  sum1 >= sum2



if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))
