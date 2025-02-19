class Dog:
    def __init__(self, name="Unknown", age=0):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name=name.upper()


if __name__ == '__main__':
    snoopy = Dog()
    snoopy.name = "Snoopy" # Calls setter

    print(snoopy.name)     # Calls getter
                           # prints 'SNOOPY'

