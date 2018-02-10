# Define la clase Punto
class Punto:
    """ Clase Punto
    """
    contPuntos = 0

    def __init__(self, x=0, y=0):
        # se accede a continuación a un atributo ("variable") de clase, compartida por todas las instancias
        Punto.contPuntos += 1
        # se accede a continuación a los atributos ("variables") de la instancia
        self.x = x
        self.y = y

    def imprimir_pto(self):
        print('Punto: (', self.x, ' , ', self.y, ')')

    def imprimir_total_ptos(self):
        print("Número de puntos creados: ", Punto.contPuntos)

    def modif_coord(self, x, y):
        self.x = x
        self.y = y

    def trasladar(self, r, q):
        self.x += r
        self.y += q

    def nuevopto_trasladar(self, r, q):
        puntoN = Punto()
        puntoN.x = self.x + r
        puntoN.y = self.y + q
        # se devuelve nuevo punto
        return puntoN

    # sobrecarga de + (operador)
    def __add__(self, pto):
        self.x += pto.x
        self.y += pto.y
        return self


if __name__ == '__main__':
    # la creación de una instancia u objeto de una clase se realiza como la invocación a una función
    # pasando los argumentos correspondientes del método __init__ salvo self
    puntoA = Punto()
    puntoB = Punto(3, 1)
    puntoB.imprimir_pto()
    print("PuntoB: (%f, %f)" % (puntoB.x, puntoB.y))
    print("Número total de puntos: ", puntoA.contPuntos)
    puntoC = puntoA + puntoB
    puntoC.imprimir_pto()
    puntoD = puntoC.nuevopto_trasladar(5, 1)
    puntoD.imprimir_pto()
