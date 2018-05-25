#Proyecto VacationDetination
#Marcos Gutierrez 		17909
#David Valenzuela		171001
#Fernando Hengsterberg	17699
from Destino import Destino
from Vacation import Vacation

#-----MAIN PARA EL USUARIO-----#

#Contadosr para el menu
run = True
v = Vacation()



#Ciclo para recorrer el contador
while run:
	print("----------------------------------------------------------------")
	print("BIENVENIDO A LA APLICACION\n ESPERO EL VIAJE SEA DE SU COMODIDAD")
	print(" 1. Elminar\n 2. Buscar\n 3. Agregar\n 4. Salir")
	opcion = input("QUE DESEA HACER?\n")
	#Opcion para eliminar destino
	if(opcion == "1"):
		nombreDestino = input("Escribra el nombre que desea eliminar:\n")
		if v.deleteDestino(nombreDestino):
			print "Eliminado correctamente"
		else:
			print "No se encontraron resultados"

	#Opcion para Buscar Destino
	if(opcion == "2"):
		#Ingresar clima
		climaN = input("Ingrese el clima (si no dessea filtrar por clima ingrese 0):\n")
		if(climaN == "0"):
			climaN = ""
		#Ingresar nombreN
		nombreN = input("Ingrese el nombre (si no desea filtrar por el nombre ingrese 0):\n")
		if(nombreN == "0"):
			nombreN = ""
		#Ingresar Ubicacion
		ubicacionN = input("Ingrse la ubicacion del destino (si no desea filtrar por la ubicacion ingrese 0):\n")
		if(ubicacionN == "0"):
			ubicacionN = ""
		#Ingresar los tag
		tagN = input("Ingrese el tag del destino (si no desea filtrar por el tag ingrese 0):\n")
		if tagN == "0":
			tagL = []
		else:
			tagL = []
			tagL.append(tagN)
			con = input("Ingresar otro tag? s/n")
			#Ciclo para ingresar n cantidad de tag
			while con == "s":
				tagN = input("Ingrese el tag de destino:")
				tagL.append(tagN)
				con = input("Ingresar otro tag? s/n\n")
		listaD = v.getDestinos(nombre=nombreN, ubicacion=ubicacionN, tags=tagL, clima=climaN)
		if len(listaD)>0:
			for element in listaD:
				print element
		else:
			print "No se econtraron resultados"

	#Opcion para agregar
	if(opcion == "3"):
		#Agregar Nombre
		nombre = input("Ingrese el nombre del destino que desea agregar: \n")
		clima = input("Ingrese el clima del destino que desea agregar: \n")
		ubicacion = input("Ingrese la ubicacion del destino que desea agregar: \n")
		tagN = input("Ingrese el tag del destino (si no desea filtrar por el tag ingrese 0):\n")
		if tagN == "0":
			tagL = []
		else:
			tagL = []
			tagL.append(tagN.uppe)
			con = input("Ingresar otro tag? s/n")
			#Ciclo para ingresar n cantidad de tag
			while con == "s":
				tagN = input("Ingrese el tag de destino:")
				tagL.append(tagN)
				con = input("Ingresar otro tag? s/n\n")
		v.addDestino(Destino(nombre, ubicacion, clima, tags=tagL))
		print "Agregado correctamente"

	if(opcion == "4"):
		run = False


t = v.getTags()
print t
for i in t:
	print i
