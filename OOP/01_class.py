# use init to declare attributes

class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

arthas = Employee("Arthas Menethil", 27)
dir(arthas)

# make a dog
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog:
    pass

a = Dog()
b = Dog()

a == b #two distinct objects in memory

# Class and Instance Attributes
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

Dog()

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)

miles.name
buddy.age
buddy.species

buddy.age = 10
buddy.age

miles.species = "Felis silvestris"
miles.species

# Instance methods
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
miles = Dog("Miles", 4)

miles.description()
miles.speak("Hello there fellow human.")

# use __str__() to control what gets printed out
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"
    

miles = Dog("Miles", 4)

print(miles)