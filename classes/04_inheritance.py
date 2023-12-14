# Parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# Child class
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


# Add __init__() function to the child class
class Student(Person):
  def __init__(self, fname, lname):         #adding the __init__ will cancel the inheritance
    Person.__init__(self, fname, lname)     #so we put the inheritance back


# super() - no need to use init, will automatically inherit properties from parent object
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)



# Add properties
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

ivan = Student("Ivan", "Hrozny")
ivan.printname()
ivan.graduationyear


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
