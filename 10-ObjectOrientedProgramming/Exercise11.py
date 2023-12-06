# 11.	Write a program in which create a TV class that describes a TV set.
# The class should contain one boolean attribute called 'is_on' that specifies whether the TV set is turned on. 
# Initially, the TV is turned off. 
# Add turn_on() and turn_off() methods in the class to turn the TV on and off, respectively. 
# Also, add a show_status() method to display whether the TV is on or off. 
# Sample message:

class TV():
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print("The TV is ON")
        else:
            print("The TV is OFF")

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

tv1 = TV("Sony")

tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.turn_off()
tv1.show_status()

# Then, try using the TV set in the program:

# a.	Create TV set
# b.	Show TV status
# c.	Turn TV on
# d.	Show TV status
# e.	Turn TV off
# f.	Show TV status
