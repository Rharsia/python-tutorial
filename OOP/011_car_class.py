# exercise - create a car class

class Car:
    def __init__(self, brand, type, fuel_type, colour):
        self.brand = brand
        self.type = type
        self.fuel_type = fuel_type
        self.colour = colour

    def __str__(self):
        return f"A {self.colour} {self.brand} {self.type} that runs on {self.fuel_type}"
    
jaguar = Car("Jaguar", "X-Type", "Diesel", "Black")
skoda = Car("Škoda", "Octavia", "Benzin", "Black")

print(jaguar)
print(skoda)