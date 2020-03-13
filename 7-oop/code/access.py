class Dog:
    def __init__(self):
        self.__name = "Unknown"
        self.__age = 10

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        if age < 20:
            self.__age = age

    def getAge(self):
        return self.__age

if __name__ == '__main__':
    snoopy = Dog()
    snoopy.setName("Snoopy")
    print(snoopy.getName())

    print(snoopy.__name) # Error!