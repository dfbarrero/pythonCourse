class Dog:
    def __init__(self):
        self._name = "Unknown"
        self.__age = 10

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setAge(self, age):
        if age > 0:
            self.__age = age

    def getAge(self):
        return self.__age

if __name__ == '__main__':
    snoopy = Dog()
    snoopy.setName("Snoopy")
    print(snoopy.getName())
    
    snoopy._name = "Laika" # No error, do not do this
    
    print(snoopy.__name) # Error!
