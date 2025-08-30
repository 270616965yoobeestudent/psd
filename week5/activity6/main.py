class Student:
    def __init__(self, name, age):
        self.name = name  # public​
        self._age = age  # protected​
        self.__grade = "A"  # private​

    def get_grade(self):
        return self.__grade

    def assign_grade(self, grade):
        self.__grade = grade


class NoGradeStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_grade(self):
        # This sub class can't use __grade from parent because it's private
        # 'self.__grade' will be an error
        return "No grade"

    def get_age(self):
        # This sub class can use _age from parent because it's protected
        return self._age


def main():
    student = Student("John", 20)
    print(student.get_grade())
    student.assign_grade("B")
    print(student.get_grade())

    no_grade_student = NoGradeStudent("Bob", 20)
    print(no_grade_student.get_grade())
    print(no_grade_student.get_age())

    # Name can directly access without using getter method
    print(no_grade_student.name)
    
    # _age should not access directly from object because it's protected
    # print(no_grade_student._age) < but this statement will not throw an error


if __name__ == "__main__":
    main()
