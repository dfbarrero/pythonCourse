class Vehicle:
	def __init__(self, wheels):
		self.wheels = wheels

class Car(Vehicle):
	def __init__(self, wheels, model):
		Vehicle.__init__(self, wheels)
		self.model = model

myBike = Vehicle(2)
ford = Car(4, "mondeo")

	
