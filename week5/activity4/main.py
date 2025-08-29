# Colour
class Colour:
    pass

class TransparentColour(Colour):
    pass

# Animal
class Animal():
    pass

class Cat(Animal, Colour):
    pass

class Dog(Animal, Colour):
    pass

class Frog(Animal, TransparentColour):
    pass

def main():
    pass


if __name__ == "__main__":
    main()
