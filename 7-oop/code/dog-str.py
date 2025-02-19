class Dog:
    def __init__(self, name="Unknown", age=0): 
        self.name = name      
        self.age = age     

    def __str__(self):  
        return self.name + ': ' + str(self.age)

    def __len__(self):
        return 1

if __name__ == '__main__':
    snoopy = Dog("Snoopy", 10) 
    print(snoopy)        # Outputs "Snoopy: 10"
    print(len(snoopy))   # Outputs "1"
