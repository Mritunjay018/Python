import math
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
       return (math.pi * self.radius) **2
    def parameter(self):
        return 2 * (math.pi*self.radius)

c = circle(5)
print(f"Area = {c.area()}")
print("parameter = ",c.parameter())

    
      
