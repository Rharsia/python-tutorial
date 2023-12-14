# Create a class
class myClass:
    x = 5

# Create an object
p1 = myClass()

p1.x

# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = "John"
        self.age = 36


p1 = Person("John", 36)

p1.name
p1.age


# The __str__() Function
# without str
class Person:
    def __init__(self, name, age):
        self.name = "John"
        self.age = 36

p1 = Person("John", 36)
print(p1)

# with str
class Person:
    def __init__(self, name, age):
        self.name = "John"
        self.age = 36

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)