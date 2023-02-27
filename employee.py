from person import Person
from uuid import uuid4


class Employee(Person):

    def __init__(self, title, firstname, lastname, dob, gender):
        super().__init__(title, firstname, lastname, dob, gender)
        self.employee_id = uuid4()

    def __str__(self):
        return f"Employee ID: {self.employee_id}, name: {self.firstname} {self.lastname}, age: {self.calculate_age()}"

    def start_work(self):
        print(f"Employee {self.employee_id} {self.firstname} {self.lastname} has started working.")


if __name__ == "__main__":
    customer1 = Employee("Ms", "Jane", "Doe", "24/03/2000", "F")
    customer2 = Employee("Mr", "Joe", "Bloggs", "24/03/1995", "M")
    print(customer1)
    print(customer2)
