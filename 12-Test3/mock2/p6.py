# (p6.py) A valid number on the planet Metis consists of digits 1 to 7 and lowercase or uppercase letters a to d. 
# A plus (+) or minus (-) sign may also appear at the beginning of the number. 
# The mnumbers array contains sample numbers. 
# Create a function f(mnumbers) that returns how many numbers in the array that are valid in the planet Metis. 
# Example:
# f(["A15","-31","7abC","+D1","-gH"])  5
# f(["A05","-3+1","7ab8C","+D1","-22k"])  1

def f(mnumbers):
    valid_count = 0

    for num in mnumbers:
        if all(char.isdigit() or char.lower() in ['a', 'b', 'c', 'd'] or char in ['+', '-'] for char in num[1:]):
            valid_count += 1

    return valid_count

if __name__ == "__main__":
    print(f(["A15", "-31", "7abC", "+D1", "-gH"]))
    print(f(["A05", "-3+1", "7ab8C", "+D1", "-22k"]))
