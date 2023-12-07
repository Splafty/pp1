# 13.	Add the set_channel(new_channel_no) method in the TV class to set the TV channel number. 
# Then try using the TV set.
# a.	Create a TV set
# b.	Show TV status
# c.	Turn TV on
# d.	Show TV status
# e.	Change TV channel to 5
# f.	Show TV status
# g.	Turn TV off
# h.	Show TV status 

class TV():
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.channel_no = 1

    def show_status(self):
        if self.is_on:
            print(f"The TV is ON, channel {self.channel_no}")
        else:
            print("The TV is OFF")

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no_):
        self.channel_no = new_channel_no_

tv1 = TV("Sony")

tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.set_channel(5)
tv1.show_status()
tv1.turn_off()
tv1.show_status()