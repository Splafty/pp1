i = 0
sum = 0
while i <= 10:
    if i%2 == 0:
        sum += i
        i += 1
    else:
        i += 1
print(f"Sum of even numbers in range <1, {i-1}> is {sum}")