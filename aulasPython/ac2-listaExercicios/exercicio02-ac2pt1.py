class Produto():
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco


class ProdutoFisico(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
        self.preco = preco

    def entregar(self):
        print(f"O produto físico está entregue.")

class ProdutoDigital(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
    def entregar(self):
        print(f"O produto digital será entregue no endereço ... ")

produto_fisico = ProdutoFisico("Livro", 29.90)
produto_digital = ProdutoDigital("iPhone 18", 40000.00)

produto_fisico.entregar()
produto_digital.entregar()
