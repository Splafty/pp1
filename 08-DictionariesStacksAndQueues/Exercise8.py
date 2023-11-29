# 8.	Create a dictionary describing your mobile phone. 
# Use at least 6 key-value pairs of data of different types. 
# Then, using 'for' loop, display the contents of the dictionary. 
# To read a key and value, use the items() method. 


mobile = {
    "OS":       "Android",
    "Producent":"Samsung",
    "Released": 2019,
    "Has5G":    False,
    "Display":  {"Type": "AMOLED", "Size": 6.4},
    "Comms":    ["WLAN", "Bluetooth", "Positioning", "NFC", "Radio", "USB"]
}

for key,value in mobile.items():
    print(f"{key} : {value}")
