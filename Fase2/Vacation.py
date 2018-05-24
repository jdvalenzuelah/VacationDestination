#Import Graph Database
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from Destino import Destino

class Vacation(object):

	#Variables "privadas"
	__db = None
	__labels = None
	__instance = None

	def __new__(cls):
		"""
		Constructor de la clase siguiendo Singleton para tener una solo instancia de la clase
		"""
		if Vacation.__instance is None:
			Vacation.__instance = object.__new__(cls)
			try:
				Vacation.__instance.__db = GraphDatabase("http://localhost:7474", username="neo4j", password="123456")
			except Exception as e:
				raise e
		Vacation.__instance.__labels = [Vacation.__instance.__db.labels.create("Destino"), Vacation.__instance.__db.labels.create("Clima"), Vacation.__instance.__db.labels.create("Ubicacion"), Vacation.__instance.__db.labels.create("Tag")]
		return Vacation.__instance

	def __addCondicional(condicionales, newCondicional):
			"""
			Metodo local para construir una cadena de condiconales en Cypher

			Argumentos:
				condicionales (str): cadena de condiciones actuales en Cypher
				newCondicional (str): nueva condicional a agregar.

			Returns:
				cadena (str) con la nuevo condicion agregada en Cypher
			"""
			#verificar si ya hay una condicon, si ya hay se agrega "AND" y una nueva, si no, se agrega la nueva condicion
			if(len(condicionales)>6):
				return (condicionales + ' AND ' + newCondicional)
			else:
				return (condicionales + newCondicional)

	def getDestinations(self, nombre="",ubicacion="",tags=[],clima=""):
		"""
		Metodo para obtener una lista de Destinos de la base de datos filtrados por nombre,
		ubicacion, clima, o tags. Los filtros son opcionales, y se pueden agregar en cualquier
		combinacion.

		Argumentos:
			nombre (str): nombre del destino (default: "")
			ubicacion (str): ubicacion del destino (default = "")
			tags (list): lista de tags para filtrar (default = [])
			clima: clima del destino (default = "")

		"""
		
		# Query en cypher base	
		baseCypher = 'MATCH (looking:Destino)-[:Clima_es]->(clima:Clima), (looking)-[:Ubicado_en]->(ubicacion:Ubicacion)'
		# Lista de condiciones
		condiciones = 'WHERE '
		# Verificamos si hay algun filtro, si lo hay se agrega a las condiciones en cypher
		if len(nombre)>0:
			condiciones = self.__addCondicional(condiciones, ('looking.name="' + nombre + '"'))
		if len(ubicacion)>0:
			condiciones = self.__addCondicional(condiciones, ('ubicacion.name="' + ubicacion + '"'))
		if len(clima)>0:
			condiciones = self.__addCondicional(condiciones, ('clima.name="' + clima + '"'))
		if len(tags)>0:
			for tag in range(len(tags)):
				baseCypher = baseCypher + ', (looking)-[:tag]->(tag' + str(tag) + ':Tag)'
				condiciones = addCondicional(condiciones, ('tag'+str(tag)+'.name="') + str(tags[tag]) + '"')
		if len(condiciones)>6:
			baseCypher = baseCypher + ' ' + condiciones
		# Agregamos el valor de retorno a la query de cypher
		baseCypher = baseCypher + ' ' + 'RETURN looking'
		# Ejecutamos la query en cypher
		query = self.__db.query(baseCypher, returns=(client.Node, str, client.Node))
		# Mapeamos los resultados a una lista de Destinos y se retorna la lista
		results = []
		for element in query:
			q = element[0]
			results.append(Destino(q["name"], q["ubicacion"], q["clima"], q["tags"]))
		return results

	def addDestino(destino):
		"""
		Metodo para agregar un nuevo destino a la base de datos, las relaciones entre nodos
		eson creadas al agregar el destino a la base de datos

		Argumentos:
			destino (Destino): destino a agregar en la base de datos

		Returns:
			Nodo recien agregado a la base de datos
		"""
		#Crear el nuevo destino
		newDestino = self.__db.nodes.create(nombre=destino.nombre, ubicacion=destino.ubicacion, clima = destino.clima, tags=destino.tags)
		self.__labels[0].add(newDestino)
		#crear nodo de propiedades
		ubicacion = self.__db.nodes.create(name=destino.ubicacion)
		clima = self.__db.nodes.create(name=destino.clima)
		tags = []
		for tag in destino.tags:
			tags.append(self.__db.nodes.create(nombre=tag))
		#Creamos las relaciones
		destino.relationships.create("Ubicado_en", ubicacion)
		destino.relationships.create("Clima_es", clima)
		for tag in tags:
			destino.relationships.create("tag", tag)
		return newDestino




	def getUbicaciones(self):
		"""
		Obtener todas las ubicaciones
		"""
		query = self.__db.query("MATCH (n :Ubicacion) return n", returns=(client.Node, str, client.Node))
		results = []
		for element in query:
			q = element[0]
			results.append(q["Ubicacion"])
		return results

