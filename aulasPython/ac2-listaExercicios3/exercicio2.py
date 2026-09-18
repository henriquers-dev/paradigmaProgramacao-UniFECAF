class FreteNormal:
	def calcular(self, valor):
		return valor * 0.05


class FreteExpresso:
	def calcular(self, valor):
		return valor * 0.10


class FreteSedex:
	def calcular(self, valor):
		return valor * 0.15


class FreteInternacional:
	def calcular(self, valor):
		return valor * 0.20


def calcular_frete(frete, valor):
	return frete.calcular(valor)


frete = FreteExpresso()
valor_frete = calcular_frete(frete, 1000)
print(valor_frete)
