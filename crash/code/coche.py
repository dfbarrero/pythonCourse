class Vehiculo:
	def __init__(self,ruedas):
		self.ruedas = ruedas

class Coche(Vehiculo):
	def __init__(self,ruedas, modelo):
		Vehiculo.__init__(self,ruedas)
		self.modelo = modelo

ford = Coche(4, "mondeo")

	
