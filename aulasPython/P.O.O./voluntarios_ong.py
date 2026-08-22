class Voluntario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.horas = 0.0000000

    def registrar_horas(self, quantidade):
        self.horas += quantidade

    def mostrar_dados(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Horas: ", self.horas)

v1 = Voluntario("Henrique", 40)
v1.registrar_horas(20.4345)
v1.mostrar_dados()