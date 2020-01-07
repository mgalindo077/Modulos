class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enMarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
			self.enMarcha, "\nAcelerando: ",self.acelera,
			"\nFrenando: ",self.frena)

class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado = cargar
		if (self.cargado==True):
			return "La Furgoneta esta cargada"
		else:
			return "La Furgoneta no esta cargada"

class Moto(Vehiculos): #Clase moto hereda de Vehiculos
	hCaballito=""

	def caballito(self):
		self.hCaballito="Haciendo caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
			self.enMarcha, "\nAcelerando: ",self.acelera,
			"\nFrenando: ",self.frena, "\n",self.hCaballito)

class VElectricos(Vehiculos):
	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando = True
