# Can't repeat as the below
# class Dog
#     def walk(self):
#         print('walk')


# class Cat:
#     def walk(self):
#         print('walk')




class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('BARK')


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()
