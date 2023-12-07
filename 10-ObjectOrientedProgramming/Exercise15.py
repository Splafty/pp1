# 15.	In the TV class, make changes to the show_status() method so that it displays not only the selected channel number but also its name. 
# When the selected channel number exceeds the list of available channels, the channel name is not displayed.
# TV is on, channel 4 (TVN)
# Then, try using the TV. 
# Set at least 7 channels (seven TV stations), change channel numbers and display TV status every time.

class TV():
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def show_status(self):
        if self.is_on:
                if self.channel_no > 0 and self.channel_no < 8:
                    print(f"The TV is ON, channel {self.channel_no} ({self.channels[self.channel_no - 1]})")
                else:
                    print(f"The TV is ON, channel {self.channel_no} ()")
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

tv1.turn_on()
tv1.set_channels(["1. TVP1", "2. TVP2", "3. Polsat", "4. TVN", "5. Filmbox", "6. Discovery", "7. Disney Channel"])
tv1.show_channels()
tv1.set_channel(0)
tv1.show_status()
tv1.set_channel(1)
tv1.show_status()
tv1.set_channel(2)
tv1.show_status()
tv1.set_channel(3)
tv1.show_status()
tv1.set_channel(4)
tv1.show_status()
tv1.set_channel(5)
tv1.show_status()
tv1.set_channel(6)
tv1.show_status()
tv1.set_channel(7)
tv1.show_status()
tv1.set_channel(8)
tv1.show_status()
tv1.turn_off()
tv1.show_status()