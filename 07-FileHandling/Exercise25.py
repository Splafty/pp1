# 25.	The announcement regarding the temperature forecast in degrees Celsius for the next three days was published on the Internet:
# "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
# Create a program that calculates the average temperature. Use regular expressions to extract the values of temperatures from the message.


import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall(r"\d{2}",message)

sum = 0

for i in range(len(temperatures)):
    sum += int(temperatures[i])
    
avarage_temperature = sum/len(temperatures)
print(avarage_temperature)
