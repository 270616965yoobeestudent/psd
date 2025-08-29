class Person:
    def __init__(self, address, name, age):
        self.name = name
        self.address = address
        self.age = age
    
    def greet(self):
        print(f"{self.name}, {self.age}, {self.address}")



class Student(Person):
    def __init__(self, address, name, age, student_id):
        super().__init__(address, name, age)
        self.student_id = student_id
    
    def greet(self):
        print(f"{self.name}, {self.age}, {self.address}, {self.student_id}")

def main():
    student = Student("717 Balloon Street", "John", 20, 'A00001')
    student.greet()


if __name__ == "__main__":
    main()
