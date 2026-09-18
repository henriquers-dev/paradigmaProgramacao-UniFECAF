class Veiculo:
    def abastecer(self):
        print("Colocando combustível...")

class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

class CarroEletrico(Veiculo):
    def abastecer(self):
        raise Exception("Carro elétrico não usa combustível.")
