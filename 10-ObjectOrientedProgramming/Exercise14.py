# 14.	In the TV class, add the channels attribute containing a list of available TV channel names (array). 
# Initially, the array should be empty (TV not programmed, no available channels). 
# Add set_channels(channels_list) and show_channels() methods in the TV class, which allows you to set channels on the TV and display the list of available channels. 
# Sample list of available channels:
# Channel list:
# 1. TVP1
# 2. TVP2
# 3. Polsat
# 4. TVN
# 5. Filmbox
# 6. Discovery
# Then, try using the TV set:
# a.	Create a TV set
# b.	Show TV status
# c.	Turn TV on
# d.	Show TV status
# e.	Display the list of available channels
# f.	Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery
# g.	Display the list of available channels
# h.	Show TV status
# i.	Turn TV offs


class TV():
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.channel_no = 1
        self.channels = []

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

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print(f"{self.channels}")


tv1 = TV("Sony")

tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.set_channels(["1. TVP1", "2. TVP2", "3. Polsat", "4. TVN", "5. Filmbox", "6. Discovery"])
tv1.show_channels()
tv1.show_status()
tv1.turn_off()
tv1.show_status()