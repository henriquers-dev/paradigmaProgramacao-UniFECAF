from abc import ABC, abstractmethod

class FreteStrategy(ABC):
    @abstractmethod

    def calcular(self):
        pass


class FreteEconomico(FreteStrategy):
    def calcular(self):
        return 10.0


class FreteExpresso(FreteStrategy):
    def calcular(self):
        return 20.0


class RetiradaLojaFisica(FreteStrategy):
    def calcular(self):
        return 0.0


class FreteEmDrone(FreteStrategy):
    def calcular(self):
        return 5.0


class Pedido:
    def __init__(self, frete: FreteStrategy):
        self.frete = frete
    
    def calcular_total(self, valor_produtos):
        if valor_produtos < 0:
            raise ValueError("Valor invalido")

        return valor_produtos + self.frete.calcular()
    
pedido1 = Pedido(FreteEconomico())
pedido2 = Pedido(FreteExpresso())
pedido3 = Pedido(RetiradaLojaFisica())
pedido4 = Pedido(FreteEmDrone())

print(f"Frete Economico: R$ {pedido1.calcular_total(100)}")
print(f"Frete Expresso: R$ {pedido2.calcular_total(100)}")
print(f"Retire na loja: R$ {pedido3.calcular_total(100)}")
print(f"Entrega via Drone: R$ {pedido4.calcular_total(100)}")
