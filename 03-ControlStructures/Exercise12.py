name1 = input("Enter first person name: ")
age1 = int(input("Enter first person age: "))
name2 = input("Enter second person name: ")
age2 = int(input("Enter second person age: "))

if age1 >= 18 and age2 >= 18:
    print(f"Both {name1} and {name2} are adults")
elif age1 >= 18 and age2 <= 18:
    print(f"{name1} is an adult but {name2} is not")
elif age1 <= 18 and age2 >= 18:
    print(f"{name1} is not an adult but {name2} is")
else:
    print(f"Both {name1} and {name2} are not adults")
