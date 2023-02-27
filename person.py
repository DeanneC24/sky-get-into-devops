from datetime import date


class Person:

    def __init__(self, title, firstname, lastname, dob, gender):
        self.title = title
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob  # string format DD/MM/YYYY
        self.gender = gender

    def calculate_age(self):
        if not isinstance(self.dob, str) or len(self.dob) != 10 or len(self.dob.split("/")) != 3:
            raise ValueError("DOB has incorrect format, string of format DD/MM/YYYY expected")

        # method that returns the person's age
        today = date.today()
        day, month, year = [int(elem) for elem in self.dob.split("/")]
        birthdate = date(year, month, day)
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


if __name__ == "__main__":
    person = Person("Ms", "Deanne", "Clarke", "24/03/19955", "F")
    print(person.calculate_age())
