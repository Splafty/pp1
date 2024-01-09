# (p7.py) A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character. Create a function f(arr) that, for a given array of usernames, returns the number of valid usernames in the array. 
# Example:
# f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]) -> 2

def f(arr):
    count = 0
    character_count = 0
    for element in arr:
        if len(element) >= 4 and len(element) <= 12:
            for character in element:
                if character.islower() or character.isdigit() or character == "_":
                    character_count += 1
        if character_count == len(element):
            character_count = 0
            count += 1
        else:
            character_count = 0
    return count



if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))