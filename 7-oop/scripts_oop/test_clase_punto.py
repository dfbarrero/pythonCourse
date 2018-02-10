from punto import Punto

puntoA = Punto(3, 9)
# puntoB = Punto(1, 9, 0)
puntoB = Punto(3, 9)

print('puntoA y puntoB son el mismo?', puntoA is puntoB)

puntoA.imprimir_total_ptos()

# variables públicas
puntoA.x = -2
puntoA.y = 3.1

print("Coordenadas cambiadas de puntoA")
puntoA.imprimir_pto()

puntoB.imprimir_pto()
# realizar traslación de puntoB
puntoB.trasladar(-0.1, 1.5)
puntoB.imprimir_pto()

puntoC = puntoB.nuevopto_trasladar(2, -2)
puntoC.imprimir_pto()

# sumamos puntos y devuelve (a puntoC o a otra variable) puntoC con la suma realizada
puntoC = puntoC + puntoA
puntoC.imprimir_pto()

puntoC.imprimir_total_ptos()

print(puntoA)
