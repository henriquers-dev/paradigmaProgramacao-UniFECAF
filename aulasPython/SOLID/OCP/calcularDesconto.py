from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular_desconto(self, valor):
        pass

class DescontoBasico(Desconto):
    def calcular_desconto(self, valor):
        return valor * 0.05

class DescontoPremium(Desconto):
    def calcular_desconto(self, valor):
        return valor * 0.10

class DescontoVIP(Desconto):
    def calcular_desconto(self, valor):
        return valor * 0.15 

class Cliente:
    
    ESTRATEGIAS = {
        "Básico": DescontoBasico(),
        "Premium": DescontoPremium(),
        "VIP": DescontoVIP(),
    }

    def __init__(self, tipo_cliente):
        self.tipo_cliente = tipo_cliente
        self.estrategia_desconto = self.ESTRATEGIAS.get(tipo_cliente)
        if self.estrategia_desconto is None:
            raise ValueError(f"Tipo de cliente desconhecido: {tipo_cliente}")

    def calcular_desconto(self, valor):
        return self.estrategia_desconto.calcular_desconto(valor)
    


cliente = Cliente("Básico")
print(cliente.calcular_desconto(100))  
