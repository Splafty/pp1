#The program asks the user to enter the temperature in Celcius scale
temperature_in_celcius = float(input("Enter the temperature in *C: "))

#The program calculates and displays the temperature in Kelvins scale
temperature_in_kelvins = temperature_in_celcius + 273.15
print(f"{temperature_in_celcius} *C equals to {temperature_in_kelvins} K")

#The program calculates and displays the temperature in Fahrenheits scale
temperature_in_fahrenheits = temperature_in_celcius*9/5+32
print(f"{temperature_in_celcius} *C equals to {temperature_in_fahrenheits} *F")