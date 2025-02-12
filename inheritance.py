class Animal:
    moves = True

    def breathe(self):
        print("Breathing")

class Fish(Animal):
    def swim(self):
        print("Swimming")

class Human(Animal):
    def walk(self):
        print("walking")

animal=Animal()
animal.breathe()

fish=Fish()
fish.swim()

human=Human()
human.walk()