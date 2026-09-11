class Entrega:
    def __init__(self, destino, peso, entregador):
        self.__destino = destino
        self.__peso = peso
        self.__entregador = entregador

    def get_destino(self):
        return self.__destino

    def get_peso(self):
        return self.__peso

    def get_entregador(self):
        return self.__entregador

    def realizar_entrega(self):
        pass


class EntregaMoto(Entrega):
    def realizar_entrega(self):
        print(f"Entrega sendo realizada de moto. "
              f"Destino: {self.get_destino()} | Peso: {self.get_peso()}kg | "
              f"Entregador: {self.get_entregador().get_nome()}")


class EntregaCaminhao(Entrega):
    def realizar_entrega(self):
        print(f"Entrega sendo realizada de caminhão. "
              f"Destino: {self.get_destino()} | Peso: {self.get_peso()}kg | "
              f"Entregador: {self.get_entregador().get_nome()}")


class Entregador:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


# Exemplo de uso
entregador1 = Entregador("Carlos")
entregador2 = Entregador("Ana")

entregas = [
    EntregaMoto("Rua A, 123", 5, entregador1),
    EntregaCaminhao("Av. B, 456", 800, entregador2)
]

for entrega in entregas:
    entrega.realizar_entrega()
