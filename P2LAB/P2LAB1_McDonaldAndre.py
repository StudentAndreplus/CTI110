import math

radius = float(input("Enter the radius of the circle: "))


diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Radius of the circle: ", radius)
print("Diameter of the circle: {:.2f}".format(diameter))
print("Circumference of the circle: ", circumference)
print("Area of the circle: {:.3f}".format(area))