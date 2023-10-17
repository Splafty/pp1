height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = (weight/height/height)*10000
print("Your BMI index: ",BMI)
is_correct = 18.5 <= BMI <= 24.9
print("Correct weight: ",is_correct)
