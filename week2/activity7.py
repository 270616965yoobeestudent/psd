class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        print(
            f"Name: {self.name}, Salary: {self.salary:.2f}, Job Title: {self.job_title}"
        )

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary increase to {self.salary:.2f}")


def main():
    employees = [
        Employee("Johnny", 500, "Senior Programmer"),
        Employee("Andrew", 300, "Junior Programmer"),
        Employee("Jenny", 100, "Project Manager"),
        Employee("Bob", 50, "Driver"),
    ]
    for employee in employees:
        employee.display_info()

    while True:
        name = input("Who do you want to increase salary: ")
        employee = next((emp for emp in employees if emp.name == name), None)
        if employee is None:
            print(f"'{name}' is not found in employees")
        else:
            employee.display_info()
            amount = float(
                input(f"How much do you want to increase salary for '{name}': ")
            )
            employee.give_raise(amount)


if __name__ == "__main__":
    main()
