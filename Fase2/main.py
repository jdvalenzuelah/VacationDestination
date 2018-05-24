from Destino import Destino
from Vacation import Vacation

v = Vacation()
v.addDestino(Destino("Prueba1", "Prueba", "Prueba", ["Prueba"]))
v.addDestino(Destino("Prueba2", "Prueba", "Prueba", ["Prueba"]))
v.addDestino(Destino("Prueba3", "Prueba", "Prueba", ["Prueba"]))

for i in v.getDestinations(clima="Prueba"):
	print i

print(v.deleteDestino("Prueba2"))
