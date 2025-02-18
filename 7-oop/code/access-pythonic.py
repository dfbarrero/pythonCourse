class Dog:
    def __init__(self, name="Unknown", age=0):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name=name.upper()


if __name__ == '__main__':
    snoopy = Dog()

    print(snoopy.name)

    snoopy.name="Snoopy"

    print(snoopy.name)

