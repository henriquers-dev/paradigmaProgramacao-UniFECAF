class Transporte:
    def __init__(self, linha, capacidade):
        self.linha = linha
        self.capacidade = capacidade

    def exibir_informacoes(self):
        print(f"Linha: {self.linha}")
        print(f"Capacidade: {self.capacidade} passageiros")

class Onibus(Transporte):
    def __init__(self, linha, capacidade):
        super().__init__(linha, capacidade)

    def transportar(self):
        print(f"Ônibus está transportando passageiros")

class Metro(Transporte):
    def __init__(self, linha, capacidade):
        super().__init__(linha, capacidade)

    def transportar(self):
        print(f"Este metrô está transportando passageiros")

class Motorista(Onibus):
    def __init__(self, linha, capacidade):
        super().__init__(linha, capacidade)

    def dirigir(self):
        print(f"O motorista está dirigindo o ônibus da linha {self.linha}")

class Condutor(Metro):
    def __init__(self, linha, capacidade):
        super().__init__(linha, capacidade)

    def conduzir(self):
        print(f"O condutor está conduzindo o metrô da linha {self.linha}")


metro = Metro("Linha 1899A", 200)
onibus = Onibus("Linha 2432", 50)
