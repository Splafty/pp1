# 46.	Write a program that displays a lottery coupon (numbers from 1 to 49) in the format as below.
#   1  8 15 22 29 36 43
#   2  9 16 23 30 37 44
#   3 10 17 24 31 38 45
#   4 11 18 25 32 39 46
#   5 12 19 26 33 40 47
#   6 13 20 27 34 41 48
#   7 14 21 28 35 42 49


i = 0
while i <= 6:
    j = 1
    while j < 50:
        print(f"{i+j:2d}", end=" ")
        j += 7
    print()
    i += 1