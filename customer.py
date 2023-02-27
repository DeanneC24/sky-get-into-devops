from person import Person
from uuid import uuid4


class Customer(Person):

    def __init__(self, title, firstname, lastname, dob, gender):
        super().__init__(title, firstname, lastname, dob, gender)
        self.customer_id = uuid4() # unique id

    def __str__(self):
        return f"Customer ID: {self.customer_id}, name: {self.firstname} {self.lastname}, age: {self.calculate_age()}"

    def make_purchase(self):
        print(f"Customer {self.firstname} {self.lastname} has made a purchase.")


if __name__ == "__main__":
    customer1 = Customer("Ms", "Jane", "Doe", "24/03/2000", "F")
    customer2 = Customer("Mr", "Joe", "Bloggs", "24/03/1995", "M")
    print(customer1)
    print(customer2)
