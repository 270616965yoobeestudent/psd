class Person:
    def __init__(self, name, age, address):
        self.personal_details = [name, age, address]

    def display(self):
        print("Name:", self.personal_details[0])
        print("Age:", self.personal_details[1])
        print("Address:", self.personal_details[2])

    def displaySentence(self):
        print(
            f"Name is {self.personal_details[0]}, {self.personal_details[1]} years old, and lives in {self.personal_details[2]}"
        )

    def addAge(self, age):
        self.personal_details[1] += age


def main():
    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")

    person = Person(name, age, address)
    person.display()

    addAge = int(input("How many years to add to your age: "))
    person.addAge(addAge)
    person.displaySentence()


if __name__ == "__main__":
    main()
