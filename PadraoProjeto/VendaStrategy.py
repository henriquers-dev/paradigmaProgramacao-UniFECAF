from abc import ABC, abstractmethod

class DescontoStrategy(ABC):
    @abstractmethod
    def calcular(self):
        pass

class DescontoComum(DescontoStrategy):
    def calcular(self):
        return 0.05

class DescontoVIP(DescontoStrategy):
    def calcular(self):
        return 0.20

class DescontoPremium(DescontoStrategy):
    def calcular(self):
        return 0.30

class Venda:
    def __init__(self, desconto: DescontoStrategy):
        self.desconto = desconto

    def calcular_valorFinal(self, valor):
        if valor < 0:
            return valor - self.desconto.calcular()
    def mudar_desconto(self, novoDesconto: DescontoStrategy):
        self.desconto = novoDesconto

venda = Venda(DescontoComum())

print(f"Desconto Comum: R$ {venda.calcular_valorFinal(50)}")
venda.mudar_desconto(DescontoComum())

print(f"Desconto VIP: R$ {venda.calcular_valorFinal(100)}")
venda.mudar_desconto(DescontoVIP())

print(f"Desconto Premium: R$ {venda.calcular_valorFinal(200)}")
venda.mudar_desconto(DescontoPremium())