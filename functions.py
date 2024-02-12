# Inbuilt functions
number = max(89, 70, 23, 45, 123)
print(number)

x = min(78, 45, 34, 1)
print(x)

z = pow(2, 3)
print(z)


# User-defined functions - They are prompted by the user
def name():
    print("Tracey")


name()  # Calling a function to show output


def student():  # One student
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


def students(name, age, course):  # Many students
    print(name, age, course)


students("Vincent", 18, "MIT")
students("June", 19, "MIT")
students("Allan", 20, "Cybersecurity")
students("David", 18, "Datascience")


def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)


employees("Joyce Munyua", 25, "Female", "HR Manager", 200000)
employees("George Lewis", 35, "Male", "CEO", 150000)
employees("Samuel Njoroge", 30, "Male", "Managing director", 200000)
employees("Emmanuel Mbadi", 23, "Male", "Auditor", 200000)
employees("Nicole Jeptoo", 21, "Female", "Secretary", 100000)
