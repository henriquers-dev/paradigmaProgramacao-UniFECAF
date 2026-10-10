from abc import ABC, abstractmethod


class Material(ABC):
	def __init__(self, titulo, autor):
		self.titulo = titulo
		self.autor = autor

	@abstractmethod
	def disponibilizar(self):
		pass

	def devolver(self):
		pass

class Biblioteca:
    def __init__(self):
        self.materiais = []

    def adicionar_material(self, material):
        self.materiais.append(material)

    def listar_materiais(self):
        for material in self.materiais:
            print(f'Título: {material.titulo}, Autor: {material.autor}')


class Livro(Material):
	def disponibilizar(self):
		print(f'Livro "{self.titulo}" de {self.autor} disponível para empréstimo.')

	def devolver(self):
		print(f'Livro "{self.titulo}" de {self.autor} devolvido à biblioteca.')


class Revista(Material):
	def disponibilizar(self):
		print(f'Revista "{self.titulo}" de {self.autor} disponível para consulta na biblioteca.')

	def devolver(self):
		print(f'Revista "{self.titulo}" de {self.autor} devolvida à biblioteca.')


class Ebook(Material):
	def disponibilizar(self):
		print(f'E-book "{self.titulo}" de {self.autor} disponível para leitura digital.')

	def devolver(self):
		print(f'E-book "{self.titulo}" de {self.autor} devolvido à biblioteca digital.')

class EmprestimoService:
    def emprestar_material(self, material):
        material.disponibilizar()

    def devolver_material(self, material):
        material.devolver()

biblioteca = Biblioteca()
emprestimo_service = EmprestimoService()

materiais = [
	Livro("Dom Casmurro", "Machado de Assis"),
	Revista("Ciência Hoje", "Vários autores"),
	Ebook("Python para Iniciantes", "Ana Silva")
]

for material in materiais:
	biblioteca.adicionar_material(material)

biblioteca.listar_materiais()

for material in materiais:
	emprestimo_service.emprestar_material(material)


for material in materiais:
	emprestimo_service.devolver_material(material)
