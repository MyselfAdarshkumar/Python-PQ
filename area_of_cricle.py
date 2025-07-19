# This script calculates the area of a circle and a rectangle based on user input.
r = int(input("Enter radious of circle"))
b = int(input("Enter breath of rectangle"))
l = int(input("Enter lenght rectangle"))

area_of_circle = 2 * 3.14 * r * r  # Note: This formula is for circumference, not area.
print("area of circle :- ", area_of_circle)

area_of_rectangle = l * b
print("area of rectangle :-", area_of_rectangle)
