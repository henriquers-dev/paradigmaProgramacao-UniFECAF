from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def abastecer(self):
        pass

class VeiculoEletrico(ABC):
    @abstractmethod
    def carregar(self):
        pass

class Carro(Veiculo):
    def abastecer(self):
        print("Abastecendo carro...")

class Moto(Veiculo):
    def abastecer(self):
        print("Abastecendo moto...")

class CarroEletrico(VeiculoEletrico):
    def carregar(self):
        print("Carregando carro elétrico...")
