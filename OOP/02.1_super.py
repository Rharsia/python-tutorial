class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks {sound}"
    
class JackRussellTerrier(Dog):
    pass
    
class WhiteSwissShepherd(Dog):
    def speak(self, sound="Woof!"):
        return f"{self.name} says {sound}"
    
luna = WhiteSwissShepherd("Luna", 3)



jim = JackRussellTerrier("Jim", 5)
jim.speak("Woof!")
luna.speak()


# Access parent class from inside a method of a child

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
    
jim = JackRussellTerrier("Jim", 5)
jim.speak()

Dog.speak(luna, sound="Arf")