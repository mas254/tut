# Classes

# Not specific to Python

# Define new types

# Basic types include numbers, strings, booleans
# Complex are lists and dictionaries

numbers = [1, 2, 3]
# numbers.
# point.get_distance

# class Point
# class EmailClient
class Point:
    def move(self):
        print('move')
    def draw(self):
        print('draw')

point1 = Point()
point1.draw()

point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 1
print(point2.x)

# Recap: Classes define new types - methods can be define in body, attributes set anywhere