# 9.	For the convenience and readability of the program code, it is possible to create a text representation of an object in the form of a string. 
# Such an object can then be used wherever string data is required, e.g. when calling print().
# Run the program below. 
# Pay attention to the __str__ method and the call of the print() function.

class University():
    
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return self.name + " is the best!"
    
my_university = University('KUE')
print(my_university)      
