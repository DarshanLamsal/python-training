class Animal():

    def __init__(self,name):
        self.name=name

    def breathe(self):
        print("Breathing")

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Barking")

class Human(Animal):
    def make_sound(self):
        print("Speaking")

class Fish(Animal):
    def make_sound(self):
        print("blub blub")

animal: Animal=Animal("Johnny")
animal.breathe()
animal.make_sound()

print()

jimmy:Animal=Dog(name="Jimmy")
jimmy.breathe()
jimmy.make_sound()

print()

ram: Animal=Human(name="ram")
ram.breathe()
ram.make_sound() 

print()

goldfish: Animal=Fish(name="Goldfish")
goldfish.breathe()
goldfish.make_sound()