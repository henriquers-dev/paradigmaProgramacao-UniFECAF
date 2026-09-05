class Prato:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Prato: {self.nome}, Preço: R${self.preco:.2f}")

class Cozinheiro:
    def preparar_prato(self, prato):
        prato.preparar()

class PratoPrincipal(Prato):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Prato Principal: {self.nome}, Preço: R${self.preco:.2f}")

    def preparar(self):
        print(f"Preparando o prato principal: {self.nome}")

class Sobremesa(Prato):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Sobremesa: {self.nome}, Preço: R${self.preco:.2f}")

    def preparar(self):
        print(f"Preparando a sobremesa: {self.nome}")

prato_principal = PratoPrincipal("Lasanha", 25.00)
sobremesa = Sobremesa("Mousse de Limão", 10.00)
