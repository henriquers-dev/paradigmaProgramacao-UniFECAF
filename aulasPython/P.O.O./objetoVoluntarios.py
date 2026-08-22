class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Henrique", 22)
p2 = Pessoa("José", 42)
p3 = Pessoa("Maria", 20)

print(p1.nome)
print(p2.nome)
print(p3.nome)