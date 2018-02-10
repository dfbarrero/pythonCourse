# clase a ser utilizada desde otros scripts
class Parcela(object):
    def __init__(self, uso_suelo, valor):
        # inicializar objetos de esta clase: constructor
        self.uso_suelo = uso_suelo
        self.valor = valor

    def valoracion(self):
        # residencia unifamiliar: RU
        if self.uso_suelo == "RU":
            tasa = 0.05
        # residencia unifamiliar: RU
        elif self.uso_suelo == "RM":
            tasa = 0.04
        else:
            tasa = 0.02
        valoracion = self.valor * tasa
        return valoracion

