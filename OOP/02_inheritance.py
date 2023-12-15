# inherit
class Parent:
    hair_color = "brown"

class Child(Parent):
    pass

Child.hair_color

# override
class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple"

Child.hair_color

# extend
class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

Child.speaks


# EXAMPLE: DOG PARK
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")
luna = Dog("Luna", 3, "White Swiss Shepherd")

print(luna)

# parent classes vs child classes
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class WhiteSwissShepherd(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
luna = WhiteSwissShepherd("Luna", 3)

luna.species
luna.name
print(luna)
luna.speak("Woof!")

type(luna)

# check is Luna is also an instance of Dog
isinstance(luna, Dog)
isinstance(luna, WhiteSwissShepherd)
isinstance(luna, JackRussellTerrier)

# PARENT CLASS FUNCTIONALITY EXTENSION
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
    
class WhiteSwissShepherd(Dog):
    def speak(self, sound="Woof!"):
        return f"{self.name} says {sound}"
    
luna = WhiteSwissShepherd("Luna", 3)
luna.speak()

miles = JackRussellTerrier("Miles", 4)
miles.speak()

