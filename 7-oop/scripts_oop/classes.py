# mínima clase en Python
class Cosa:
    pass

cosa1 = Cosa()
cosa2 = Cosa()
cosa3 = cosa2
print(cosa1)
print(cosa2)
print(type(cosa1))
print(cosa1 == cosa2)
print(cosa2 == cosa3)
print(cosa1 is cosa2)
print(cosa3 is cosa2)
