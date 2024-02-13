class Person:
    def __init__(self, firstname, age, gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender

    def details(self):
        print(self.firstname, "is studying")


teacher = Person("Joe", 34, "Male")
accountant = Person("Mary", 25, "Female")
doctor = Person("John", 45, "Male")

print(teacher.firstname, teacher.age, teacher.gender)
print(accountant.firstname, accountant.age, accountant.gender)
