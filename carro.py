"""
CRIAR UMA CLASSE CHAMADA CARRO:
ATRIBUTOS:
    - COR;
    - MODELO;
    - ANO;

MÉTODOS:
    - MOSTRAR DADOS;
    - LIGAR CARRO;
"""

class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
    
    def mostrar_dados(self):
        print("Cor: ", self.cor)
        print("Modelo: ", self.modelo)
        print("Ano: ", self.ano)

    def ligar_carro(self):
        print("rrrr rrrr vrummmmmm!!!")

c1 = Carro("vermelho", "Fiat Uno", 2024)
c1.mostrar_dados()
c1.ligar_carro()