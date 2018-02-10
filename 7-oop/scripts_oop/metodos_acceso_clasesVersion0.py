# Uso de métodos get() y set() para implementar la encapsulación de datos:
# ocultamiento de atributos y métodos de un objeto; sólo se puedan cambiar
# por los métodos definidos para la clase
# Se trata de proteger los datos de un objeto de su modificación por alguien
# que no tenga acceso a ellos eliminando así efectos secundarios.
# El usuario de la clase obvia la implementación de métodos y propiedades y
# sólo se preocupa de su USO. Se evita además la modificación de forma incontrolada
# Solución no muy elegante. Mejor version 1

class ClaseP:
    
    def __init__(self, x):
        self.setP(x)

    # método de acceso (getters o accessors) sirven para acceder a las propiedades privadas de un objeto -> get
    def getP(self):
        return self.__x

    # método de mutación (setters o mutators) sirven para cambiar las propiedades (privadas) de un objeto -> set
    def setP(self, x):
        if x < 0:
            self.__x = 0
        elif x > 500:
            self.__x = 500
        else:
            self.__x = x

x1 = ClaseP(-1)
print(x1.getP())

x2 = ClaseP(501)
print(x2.getP())

x1.setP(60)
print(x1.getP())

x2.setP(-200)
print(x2.getP())


# no se puede realizar la operación siguiente porque x no es atributo. Se debería dejar hacer en este escenario ... version 1
# x1.x = x1.x + x2.x


