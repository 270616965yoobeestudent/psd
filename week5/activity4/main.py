class Colour:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"{self.name}"


class TransparentColour(Colour):
    def __init__(self, name, opacity):
        super().__init__(name)
        self.opacity = opacity

    def info(self):
        return f"{self.name} with opacity {self.opacity}%"


class Animal:
    def __init__(self, species, colour):
        self.species = species
        self.colour = colour

    def info(self):
        return f"{self.species}, colour: {self.colour.info()}"


class Zoo:
    def __init__(self, name, animals):
        self.name = name
        self.animals = animals

    def show_animals(self):
        for animal in self.animals:
            print(animal.info())


def main():
    zoo = Zoo(
        "My Zoo",
        [
            Animal("Lion", Colour("Yellow")),
            Animal("Frog", TransparentColour("Green", 0.7)),
            Animal("Elephant", Colour("Gray")),
            Animal("Parrot", Colour("Red")),
            Animal("Tiger", Colour("Orange")),
            Animal("Zebra", Colour("Black and White")),
            Animal("Giraffe", Colour("Tan")),
            Animal("Penguin", Colour("Black and White")),
            Animal("Peacock", Colour("Blue")),
            Animal("Chameleon", TransparentColour("Green", 0.5)),
            Animal("Crocodile", Colour("Green")),
            Animal("Kangaroo", Colour("Brown")),
            Animal("Panda", Colour("Black and White")),
            Animal("Flamingo", Colour("Pink")),
            Animal("Wolf", Colour("Gray")),
            Animal("Otter", TransparentColour("Brown", 0.8)),
            Animal("Koala", Colour("Gray")),
            Animal("Snake", TransparentColour("Green", 0.6)),
            Animal("Turtle", TransparentColour("Olive", 0.5)),
            Animal("Octopus", Colour("Purple")),
            Animal("Rabbit", Colour("White")),
            Animal("Hyena", Colour("Spotted Brown")),
        ],
    )
    zoo.show_animals()


if __name__ == "__main__":
    main()
