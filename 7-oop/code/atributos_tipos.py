class ClaseP:
    def __init__(self):
        # los atributos privados comienzan por __. Fuera de la clase son inaccesibles o invisibles
        # solo pueden ser accedidos dentro de la clase
        self.__privado = "Atributo privado"

        # los atributos protegidos o restringidos solo pueden ser accedidos desde las subclases
        # cuando éstas las hay y herencia; también desde fuera
        self._protegido = "Atributo protegido"

        # comienzan por una letra. Son accesibles dentro de la definicion de la clase y fuera
        self.publico = "Atributo publico"

    def __printx1(self):
        print(self.__privado)

    def printx2(self):
        self.__printx1()


x = ClaseP()

x._protegido += ' y pueden modificarme'
print(x._protegido)

x.publico += ' y pueden modificarme'
print(x.publico)

# se pueden acceder a objetos privados mediante _nameclass__atributo pero NO se debe hacer!
#print(x.__privado)
#x.__privado += ' y pueden modificarme'
#print(x.__privado)

# printx2() puede ser invocado, es público y él sí que puede invocar desde la clase a __printx1()
x.printx2()

# __printx1() privado. No puede ser invocado desde fuera de la clase
x.__printx1()
