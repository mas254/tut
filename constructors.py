class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')

# Can create point object without x or y coordinate

# Broken:
# point = Point()
# print(point.x)

# point = Point(10, 20)
# print(point.x)

class Point:
    def __init__(self, x, y):
        self.x = x
        # This is the same as point.x = 10
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')

point = Point(10, 20)
print(point.x)

# Can update by doing point.x = 11

class Person:
    def talk(self):
        print('talk')

john = Person()
john.talk()

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('talk')

buyer = Person('John Smith')
print(buyer.name)
buyer.talk()

# Making a more complex message

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Name: {self.name}')

buyer2 = Person('John Smith')
buyer2.talk()

bob = Person('Bob')
bob.talk()