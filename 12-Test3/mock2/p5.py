# (p5.py) Class C describes a point (x,y) in the plane. 
# The point coordinates are given when creating (initializing) the object. 
# The class contains the m1() method that returns the number of the quadrant of the Cartesian system in which the point (x,y) is located ( https://en.wikipedia.org/wiki/Quadrant_(plane_geometry) ). 
# The m1() method returns 0 if the point (x,y) is located on the X-axis or Y-axis. 
# The class contains the m2(a,b) method that returns true when the point (x,y) is in the same quadrant of the Cartesian system as the point with coordinates a,b. 
# Otherwise, the method returns false. 
# The class contains the m3(a,b) method that returns true when the distance between points (x,y) and (a,b) is greater than 5. 
# Otherwise, the method returns false. 
# Example:
# p = C(2,3)
# p.m1()  1
# p.m2(7,4)  True
# p.m2(-3,1)  False
# p.m3(8,5)  True
# p.m3(4,7)  False
# p1 = C(0,5)
# p1.m1()  0
# p1.m2(4,7)  False
# p1.m2(-7,0)  True

import math

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0

    def m2(self, a, b):
        return self.m1() == C(a, b).m1()

    def m3(self, a, b):
        distance = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return distance > 5

if __name__ == "__main__":
    p = C(2, 3)
    print(p.m1())
    print(p.m2(7, 4))
    print(p.m2(-3, 1))
    print(p.m3(8, 5))
    print(p.m3(4, 7))

    p1 = C(0, 5)
    print(p1.m1()) 
    print(p1.m2(4, 7))
    print(p1.m2(-7, 0))
