class Dog:
    def __init__(self): # Constructor
        self.name = "Unknown" # Attribute
        self.age = 10         # Attribute

    def bit(self):            # Method
        print(self.name + " has bitten")

    def describe(self):       # Method
        print("Name: ", self.name)
        print("Age: ", self.age)

if __name__ == '__main__':
    snoopy = Dog() # Instanciate class Dog ...
    laika = Dog()  # snoopy and laika are objects

    snoopy.name = "Snoopy"
    snoopy.age = 4

    laika.name = "Laika"

    snoopy.bit()

    snoopy.describe()
    print() # Print empty line
    laika.describe()
