# 8.	Identify at least 3 states and 3 behaviors for a telephone object. 
# Then, for the listed states and behaviors, create a class with fields (attributes) and methods. 
# Try to use verbs in method names as they describe activities. 
# Finally, create a object, call its methods and display object’s properties.

class Phone():
    def __init__(self,brand,model,production_year):
        self.brand = brand
        self.model = model
        self.production_year = production_year
        self.is_on = False
        self.running_app = "None"

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def open_app(self, app):
        self.running_app = app
    
    def close_app(self):
        self.running_app = "None"



telephone = Phone("Samsung","S10+",2019)

print(f"My phone's brand is: {telephone.brand}.")
print(f"It's model is: {telephone.model}.")
print(f"It was produced in: {telephone.production_year}.")
print()

print(f"Is the telephone turned on: {telephone.is_on}")
telephone.turn_on()
print(f"Is the telephone turned on: {telephone.is_on}")
print()

print(f"Currently running app: {telephone.running_app}")
telephone.open_app("YouTube")
print(f"Currently running app: {telephone.running_app}")
telephone.close_app()
print(f"Currently running app: {telephone.running_app}")
print()

print(f"Is the telephone turned on: {telephone.is_on}")
telephone.turn_off()
print(f"Is the telephone turned on: {telephone.is_on}")
