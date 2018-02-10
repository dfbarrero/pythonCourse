class Persona():
    direccion = "Calle ..." #atributo de la clase; fuera de los métodos
    def __init__(self, nombre, edad):
        # atributos de objeto
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return("Nombre: {0:10}\t Edad: {1:2}\t Dirección: {2:20}".\
               format(self.nombre, self.edad, self.direccion))

persona1 = Persona("José", 48)
persona2 = Persona("María", 16)
persona3 = Persona("Ángel", 31)

# Para persona1 se cambia el atributo de la clase y pasa a ser un atributo de objeto
# para las demas personas, sigue siendo el mismo atributo de clase y con el mismo valor
persona1.direccion = "Avenida ...."
for persona in [persona1, persona2, persona3]:
    print(persona)

print('=' * 50)

# Ahora cambiamos el atributo de clase directamente
# pero para persona1, su atributo de objeto direccion oculta el de la clase
Persona.direccion = "Carretera ...."
for persona in [persona1, persona2, persona3]:
    print(persona)

print('=' * 50)

# Y ahora se bora el atributo de objeto de persona1 por lo que todos los objetos Persona
# tendrán el atributo de clase direccion

del persona1.direccion
for persona in [persona1, persona2, persona3]:
    print(persona)

print('=' * 50)

