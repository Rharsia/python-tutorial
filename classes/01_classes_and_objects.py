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

# Modify object properties
print(p1.name, p1.age)

p1.age = 40

print(p1.name, p1.age)

# Delete object properties
del p1.age

# Delete Objects
del p1

# Pass statement - class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class notReady():
    pass