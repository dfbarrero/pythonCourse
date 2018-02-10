class Rio:
	#Constructor de la clase.
	def __init__(self,nombre,longitud):
		self.nombre = nombre
		self.__longitud = longitud		
	#Metodos get de la clase Rio.
	def getNombre(self):
		return self.nombre
	def getLongitud(self):
		return self.__longitud
	def setLongitud(self,longitudRio):
		self.__longitud=longitudRio


class Afluente(Rio):
	#Constructor de la clase. Llama al constructor de Rio 
	def __init__(self,nombre,longitud):
		Rio.__init__(self,nombre,longitud)
	#Metodos get de la clase Rio.
	def getNombre(self):
		return self.nombre
	def getLongitud(self):
		return self.__longitud
	def setLongitud(self,longitudRio):
		self.__longitud=longitudRio

#Instancias de los animales.
tajo = Rio('Tajo',1038)
tajo.setLongitud(1034)
#Impresion por pantalla.
print(tajo.getNombre())
print(tajo.getLongitud())
jarama = Afluente("Jarama", 190)
print(jarama.getLongitud()) #Esto falla porque el atributo es privado.