# 36.	A device in a door registers people entering and leaving a room. 
# The + sign means a person entering a room and the – sign a person leaving a room. 
# Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise. 
# Sample result:
# f("+-+++-+---") returns True
# f("+-+-+-+-") returns False
# f("+-++-+--") returns False
# f("+-++-++-+---") returns True

import doordetector

detector = "+-+++-+---"
three_or_more = doordetector.f(detector)
print(f"f({detector}) returns {three_or_more}")

detector = "+-+-+-+-"
three_or_more = doordetector.f(detector)
print(f"f({detector}) returns {three_or_more}")

detector = "+-++-+--"
three_or_more = doordetector.f(detector)
print(f"f({detector}) returns {three_or_more}")

detector = "+-++-++-+---"
three_or_more = doordetector.f(detector)
print(f"f({detector}) returns {three_or_more}")