class Destino(object):
	"""
	Destino posible al que se puede ir.

	Attributes:
		nombre (String): nombre del destino.
		ubicacion (String): ubicacion deonde se encuentra.
		tags (list): categorias a las cuales puede ser asignado el destino.
		clima (String): clima del destino.

	"""

	def __init__(self, nombre, ubicacion, clima, tags=[]):
		"""
		Constructor de la clase 
		"""
		self.nombre = nombre.upper()
		self.ubicacion = ubicacion.upper()
		self.tags = tags
		self.clima = clima.upper()

	def __str__(self):
		"""
		toString
		"""
		listStr = ""
		for element in self.tags:
			listStr = listStr + str(element) + ', '
		listStr = listStr[:-2]
		return "Nombre: %s Ubicacion: %s Clima: %s Tags: %s" %(self.nombre, self. ubicacion, self.clima, listStr)
