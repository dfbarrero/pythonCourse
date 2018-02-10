#Gato hereda de animal
class Gato(Animal):
	#Constructor de la clase. Llama al constructor de Animal 
	def __init__(self,patas):
		Animal.__init__(self,"Gato",patas)
		self.sonido='miau'
	#Metodos propios de la clase gato.
	def maullar(self):		
		print self.sonido
#Instancias de los gatos.
gatoConBotas = Gato(2)
#Impresion por pantalla.
gatoConBotas.maullar()
print gatoConBotas.getTipo()



