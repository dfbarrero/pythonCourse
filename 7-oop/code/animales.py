class Animal:
	#Constructor de la clase.
	def __init__(self,tipo,patas):
		self.tipo = tipo
		self.patas = patas		
	#Metodos get de la clase Animal.
	def getTipo(self):
		return self.tipo
	def getPatas(self):
		return self.patas
		
#Instancias de los animales.
snoopy = Animal('Perro',4)
gatoComun = Animal("Gato",4)
#Impresion por pantalla.
print snoopy.getTipo()
print gatoComun.getPatas()