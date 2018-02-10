from punto import Punto
from triangulo import Triangulo

puntoA = Punto(3, 9)
# puntoB = Punto(1, 9, 0)
puntoB = Punto(3, 9)

# Crear dos triángulos con cuatro puntos
puntoA = Punto(0.0, 0.0)
puntoB = Punto(6, 0.2)
puntoC = Punto(3.5, 6.5)
puntoD = Punto(8.1, 3.6)

trianguloA = Triangulo(puntoA, puntoB, puntoC)
trianguloB = Triangulo(puntoB, puntoD, puntoC)

# Imprimir las coordenadas y área de cada triángulo
for i in [trianguloA, trianguloB]:
    i.imprimir_ptos()
    print("Area del triángulo: ", i.area())

print("Modificar las coordenadas de puntoB -> se modifican los triángulos porque referencian el mismo objeto")
print(puntoB.modif_coord(5, -0.1))

for i in [trianguloA, trianguloB]:
    i.imprimir_ptos()
    print("Area del triángulo: ", i.area())

print("Modificar las coordenadas de puntoC pero en el triángulo trianguloA")
print(trianguloB.modificar_coord_pto(2, 2.5, 8.3))

for i in [trianguloA, trianguloB]:
    i.imprimir_ptos()
    print("Area del triángulo: ", i.area())
