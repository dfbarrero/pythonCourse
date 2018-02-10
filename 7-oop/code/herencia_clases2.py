class Persona:
    nombre = ""
    def __init__(self, nomPersona):
        self.nombre = nomPersona
        print("Se ha creado una persona")

    def imprimir(self):
        print(self.nombre)

# la subclase hija Empleado puede llamar a los métodos de la clase Padre de varias maneras
# Aquí una de ellas...

class Empleado(Persona):
    nombrePuesto = ""

    # se invoca al método imprimir de Persona, en vez del suyo propio de esta forma
    def __init__(self, nompersona="", nombreCargo=""):
        self.nombrePuesto = nombreCargo
        Persona.__init__(self, nompersona)
        print("Empleado creado")

    def imprimir(self):
        print(self.nombre, self.nombrePuesto)

class Cliente(Persona):
    email = ""
    direccion = ""

    def imprimir(self):
        print(self.nombre, self.direccion, self.email)


empleado1 = Empleado("Manuel Soto")
empleado1.nombrePuesto = "Analista"
empleado1.imprimir()

empleado2 = Empleado("Juan Ignacio Valbuena", "Arquitecto")
empleado2.imprimir()