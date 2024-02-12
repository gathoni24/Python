# Data Types
number = 45  # int
num = 56.78  # float
greeting = "Hello there"  # str
isPythonInteresting = True  # bool

# Variable storing multiple values
languages = ["python", "php", "java"]  # List
fruits = ("apple", "banana", "pineapple")  # Tuple
countries = {"Kenya", "China", "USA"}  # Set

# Dictionary
details = {
    "firstname": "Grace",
    "age": 17,
    "course": "MIT",
    "nationality": "North American"
}

print(number)
print(greeting)
print(countries)
print(isPythonInteresting)
print(details)
print(details ["nationality"])
print(details ["course"])

# Determining the data types
print(type(details))
print(type(countries))

# Type casting - converting one data type to another
print(float(number))
print(int(num))

