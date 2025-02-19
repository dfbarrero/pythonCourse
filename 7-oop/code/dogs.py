class Dog:
    def __init__(self, name="Unknown", age=0): 
        # Constructor
        self.name = name      # Attribute
        self.age = age        # Attribute

    def bit(self):            # Method
        print(self.name + " has bitten")

    def describe(self):       # Method
        print("Name: ", self.name)
        print("Age: ", self.age)

if __name__ == '__main__':
    snoopy = Dog() # Instanciate class Dog ...
    laika = Dog("Laika")  
    # snoopy and laika are objects

    snoopy.name = "Snoopy"
    snoopy.age = 4

    snoopy.bit()
    snoopy.describe()

    print() # Print empty line
    laika.age = 10
    laika.describe()
