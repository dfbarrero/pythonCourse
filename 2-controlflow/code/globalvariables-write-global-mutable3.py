lista = ["Juan", "Pepe"]

def f():
    global lista
    lista = ["Maria"]

print(lista)
f()
print(lista)