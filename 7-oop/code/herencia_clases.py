class Persona:
    nombre = ""
    def __init__(self, nomPersona):
        self.nombre = nomPersona
        print("Se ha creado una persona")

    def imprimir(self):
        print(self.nombre)

# se definen dos subclases con la clase padre Persona entre paréntesis
# los métodos se heredan pero cuando la clase hija define (este caso) un método
# con el mismo nombre que uno de la clase Padre, se sustituye éste
# por el método de la clase hija de igual nombre

class Empleado(Persona):
    nombrePuesto = ""

    def imprimir(self):
        print(self.nombre, self.nombrePuesto)

class Cliente(Persona):
    email = ""
    direccion = ""

    def imprimir(self):
        print(self.nombre, self.direccion, self.email)

persona1 = Persona("Juan Sanz")
persona1.imprimir()

empleado1 = Empleado("Manuel Soto")
empleado1.nombrePuesto = "Analista"
empleado1.imprimir()

cliente1 = Cliente("Ana Sánchez")
cliente1.direccion = "C/ Pepito de los Palotes, nº 43, bajo C"
cliente1.email = "pepitopalotes@sam.com"
cliente1.imprimir()