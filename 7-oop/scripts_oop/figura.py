class Figura(object):
    def __init__(self, c, b):
        self.__color = c
        self.__borde = b

    def get_color(self):
        print("metodo get_color")
        return self.__color

    def set_color(self, valor):
        print("metodo set_color")
        self.__color = valor

    color = property(fget = get_color, fset = set_color)

    def get_borde(self):
        print("metodo get_border")
        return self.__borde

    borde = property(fget = get_borde)

if __name__=='__main__':
    figuraA = Figura('rojo', True)
    print(figuraA.color)
    print(figuraA.borde)
    figuraA.color = "verde"
    print(figuraA.color)
    figuraA.borde = False # error, no se puede establecer el valor del atributo; sí obtenerlo