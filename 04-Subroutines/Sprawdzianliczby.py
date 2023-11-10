# Zbiór od 5 do 20 np

def f(x, y):
    final = ""
    for i in range (x, y+1):
        if i % 2 == 1:
            final += str(i) + ","
    return final

x = 5
y = 20
print(f(x, y))