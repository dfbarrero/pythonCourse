from punto import Punto
# Define la clase Triangulo
class Triangulo:
    """ Clase Triangulo
    """

    def __init__(self, puntoA, puntoB, puntoC):
       self.ptos_triangulo = [puntoA, puntoB, puntoC]

    def imprimir_ptos(self):
        print('Puntos del triángulo: ')
        for i in self.ptos_triangulo:
            i.imprimir_pto()

    def modificar_coord_pto(self, indpto, x, y):
       self.ptos_triangulo[indpto].modif_coord(x, y)

    def area(self):
        ptos_triang = self.ptos_triangulo
        x1 = ptos_triang[1].x - ptos_triang[0].x
        y1 = ptos_triang[1].y - ptos_triang[0].y
        x2 = ptos_triang[2].x - ptos_triang[0].x
        y2 = ptos_triang[2].y - ptos_triang[0].y

        return abs(x1 * y2 - x2 * y1)

