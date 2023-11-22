# 23.	Create a program that saves to a text file integer numbers in the range <1,10> with their second and third power. 
# Sample result:
# 1,1,1
# 2,4,8
# 3,9,27
# 4,16,64
# …

with open("numbersandpowers.txt", "w") as f1:
    for i in range(1,11):
        f1.write(f"{i},{i**2},{i**3} \n")