# Uso de métodos get() y set() para implementar la encapsulación de datos:
# ocultamiento de atributos y métodos de un objeto; sólo se puedan cambiar
# por los métodos definidos para la clase
# Se trata de proteger los datos de un objeto de su modificación por alguien
# que no tenga acceso a ellos eliminando efectos secundarios.
# El usuario de la clase obvia la implementación de métodos y propiedades y
# sólo se preocupa de su USO. Se evita además la modificación de forma incontrolada

class ClaseP:
    # se hace x publica en vez de establecer self.__x = x para poder acceder a x fuera así: x1.x (x1 objeto de ClaseP)
    def __init__(self, x):
        self.x = x

    # Se necesita chequear con los dos métodos siguientes el límite de los valores de x
    # los dos métodos tienen el mismo nombre y DIFERENTE NÚMERO DE PARÁMETROS. ESTO ES POSIBLE GRACIAS Al
    # establecimiento de "decoradores" (@property y @x.setter). Supone SOBRECARGA DE FUNCIONES
    @property # decorador
    # método de acceso (getters o accessors) sirven para acceder a las propiedades privadas de un objeto -> get
    def x(self):
        return self.__x

    @x.setter # decorador
    # método de mutación (setters o mutators) sirven para cambiar las propiedades (privadas) de un objeto -> set
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 500:
            self.__x = 500
        else:
            self.__x = x

x1 = ClaseP(-1)
print(x1.x)

x2 = ClaseP(501)
print(x2.x)


x1.x = 600
print(x1.x)

x1.x = -4
print(x1.x)

x1.x = 80
print(x1.x)

x1.x = x1.x + x2.x
print(x1.x)

