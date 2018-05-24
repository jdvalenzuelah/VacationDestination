from Destino import Destino
from Vacation import Vacation


#nombre,ubicacion,clima,[tag1,tag2]
def parseDestino(cadena):
	"""
	Metodo para convertir un string a un objeto Destino.
	string debe ser de la forma:
		nombre,ubicacion,clima,[tag1,tag2]

	Argumentos:
		str (str): string a convertir a Destino
	"""
	if len(cadena)>0:
		try:
			#pasamos todo a mayusculas
			cadena = cadena.upper()
			#Separar los atibutos de los tags
			cadena = cadena.split("[")
			#removemos el carater ]
			cadena[1] = cadena[1][:-1]
			# Separamos los atributos y los tags
			atributos = cadena[0].split(",")
			tags = cadena[1].split(",")
			#lo mapeamos a un destino
			destino = Destino(atributos[0], atributos[1], atributos[2], tags)
			return destino
		except Exception as e:
			print("String no esta en el formato correcto")
			return None
	else:
		return None

def parseFile(filePath):
	"""
	Parse el contenido de un archivo de texto, el archivo debe de contener en cada una de las ineas
	el string a parsear en el formato correcto (nombre,ubicacion,clima,[tag1,tag2]).
	Metodo anade cada uno de los objetos parseados a la base de datos de Vacation.

	Argumetnos:
		filePath (str): direccion del archivo que se leera
	"""
	v = Vacation()
	with open(filePath) as f:
		for line in f:
			v.addDestino(parseDestino(line.strip().upper()))


parseFile("database.txt")
print "Finalizado"
