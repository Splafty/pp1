# 36.	A device in a door registers people entering and leaving a room. 
# The + sign means a person entering a room and the – sign a person leaving a room. 
# Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise. 
# Sample result:
# f("+-+++-+---") returns True
# f("+-+-+-+-") returns False
# f("+-++-+--") returns False
# f("+-++-++-+---") returns True

def f(detector):
    number_of_people = 0
    for letter in detector:
        if letter == "+":
            number_of_people += 1
        else:
            number_of_people -= 1
        
        if number_of_people == 3:
            return True
    return False

if __name__ == "__main__":
    detector = "+-+++-+---"
    three_or_more = f(detector)
    print(f"f({detector}) returns {three_or_more}")

    detector = "+-+-+-+-"
    three_or_more = f(detector)
    print(f"f({detector}) returns {three_or_more}")

    detector = "+-++-+--"
    three_or_more = f(detector)
    print(f"f({detector}) returns {three_or_more}")

    detector = "+-++-++-+---"
    three_or_more = f(detector)
    print(f"f({detector}) returns {three_or_more}")