from Destino import Destino
from Vacation import Vacation

v = Vacation()

for i in v.getDestinations(tags = ["MUSEOS"]):
	print i
