# Hasło ma mieć 6 znaków wsyztskie różne

password = "abcdff"

def f(password):
    unique_chars = set()

    for char in password:
        unique_chars.add(char)

    if len(unique_chars) == 6:
        return True
    else:
        return False


print(f(password))