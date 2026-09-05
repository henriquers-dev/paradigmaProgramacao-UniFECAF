class Publicacao:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Ano: {self.ano}")


class Livro(Publicacao):
    def __init__(self, titulo, ano, autor):
        super().__init__(titulo, ano)
        self.autor = autor

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Autor: {self.autor}")

class Revista(Publicacao):
    def __init__(self, titulo, ano, edicao):
        super().__init__(titulo, ano)
        self.edicao = edicao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Edição: {self.edicao}")

Livro = Livro("O Senhor dos Anéis", 1954, "J.R.R. Tolkien")
Revista = Revista("Revista Autismo", 2026, "Autismo não é doença")

Livro.exibir_informacoes()
Revista.exibir_informacoes()
