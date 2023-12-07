# 12.	In the TV class, add the channel_no attribute indicating the number of the TV channel displayed by the TV set. 
# Initially, the TV is set to channel 1.
# Modify the show_status() method so that it also displays the TV channel number, but only if the TV is turned on:
# TV is on, channel 1
# Then, try using the TV set.


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

tv1 = TV("Sony")

tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.turn_off()
tv1.show_status()

