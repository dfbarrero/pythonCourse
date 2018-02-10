class Bicicleta: #Clase
	velocidad = 2 #Atributo y asignacion int

	def __init__(self,velocidadB): #Constructor
		self.velocidad=velocidadB
	
	def reducirVelocidad(self): #Metodo propio
		self.velocidad = self.velocidad -1
	
	def imprimirVelocidad(self):
		print (self.velocidad)
	
if  __name__ =='__main__': #Main
	a = Bicicleta(4) #Instancia
	a.reducirVelocidad()
	a.imprimirVelocidad() 