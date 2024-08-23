import numpy
class Circle:
    def __init__(self, radius=float, color=str):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def getArea(self):
        return numpy.pi * (self.radius ** 2)

circulo = Circle(5.0, "green")

print(circulo.getArea())
print(circulo.getRadius())