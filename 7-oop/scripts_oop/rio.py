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
	def __init__(self,nombre,nombreRio, longitud):
		Rio.__init__(self,nombre,longitud)
		self.afluenteDeRio = nombreRio


#Instancias de las clases Rio y Afluente
tajo = Rio('Tajo',1038)
tajo.setLongitud(1034)
#Impresion por pantalla.
print(tajo.getNombre())
print(tajo.getLongitud())

jarama = Afluente("Jarama","Tajo", 190)
print(jarama.getNombre())
print(jarama.getLongitud())
print(jarama.afluenteDeRio)
print(jarama.__longitud) #Esto falla porque el atributo es privado.