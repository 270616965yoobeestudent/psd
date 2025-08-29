# People is base class that includes address, name and age
class People:
    def __init__(self, address, name, age):
        self.name = name
        self.address = address
        self.age = age


# Student is also people who has address, name and age including academic record
class Student(People):
    def __init__(self, address, name, age, academic_record):
        super().__init__(address, name, age)
        self.academic_record = academic_record


# Academic is also people who has address, name and age including tax_code and salary
class Academic(People):
    def __init__(self, address, name, age, tax_code, salary):
        super().__init__(address, name, age)
        self.tax_code = tax_code
        self.salary = salary


# GeneralStaff is also people who has address, name and age including tax_code and pay_rate
class GeneralStaff(People):
    def __init__(self, address, name, age, tax_code, pay_rate):
        super().__init__(address, name, age)
        self.tax_code = tax_code
        self.pay_rate = pay_rate


def main():
    student = Student("717 Balloon Street", "John", 20, [0.1, 0.2, 0.3])
    academic = Academic("711 Balloon Street", "Bob", 25, "55123", 10000)
    generalStaff = GeneralStaff("715 Balloon Street", "Macky", 32, "11222", 1000)
    print(student.name)
    print(academic.name)
    print(generalStaff.name)


if __name__ == "__main__":
    main()
