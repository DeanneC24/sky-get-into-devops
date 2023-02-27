from person import Person
from employee import Employee
from customer import Customer

person = Person("Ms", "Person", "One", "24/03/2000", "F")
employee = Employee("Ms", "Employee", "One", "24/03/2000", "F")
customer = Customer("Ms", "Customer", "One", "24/03/2000", "F")

print(person, f"Type: {type(person)}")
print(employee, f"Type: {type(employee)}")
print(customer, f"Type: {type(customer)}")

# all three types have access to calculate_age function from Person
print(person.calculate_age())
print(customer.calculate_age())
print(employee.calculate_age())

# employees have another function called Work and additional state called employee id
print(employee.start_work())

# customers have another function called make_purchase and additional state called customer id
print(customer.make_purchase())
