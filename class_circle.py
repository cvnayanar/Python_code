#Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.

class circle():
    def __init__(self,r):
        self.radius = r
    def get_Area(self):
        self.area = 3.14 *(self.radius**2)
        print(self.area)

    def getCircumference(self):
        circ = 2 * 3.14 * self.radius
        print(circ)
rad = circle(50)  # input radius =50
circle.get_Area(rad)
circle.getCircumference(rad)
