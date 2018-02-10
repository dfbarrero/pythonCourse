from punto import Punto
# Define la clase Triangulo
class Poligono:
    """ Clase Poligono
    """

    def __init__(self, nptos=0):
       self.numptos = nptos # variable publica
       self.__color = 'azul' #  variable pseudo_privada

    def get_color(self):
        return self.__color

    def self_color(self, col):
       self.color = col

poligA = Poligono()
print("Número de puntos", poligA.numptos)
print("Color del polígono", poligA.get_color())
print("Color del polígono", poligA.__color) # no es posible acceder desde fuera de la clase a prop. privada