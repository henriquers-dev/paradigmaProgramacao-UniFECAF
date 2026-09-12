class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self):
        print(f"{self.nome} realiza um ataque poderoso!")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self):
        print(f"{self.nome} lança um feitiço mágico!")


guerreiro = Guerreiro("Draco", 100)
mago = Mago("Dumbledore", 80)
