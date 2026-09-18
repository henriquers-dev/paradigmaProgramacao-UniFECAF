"""
Exemplo de aplicacao do SRP e do OCP.

SRP: os funcionarios calculam apenas o proprio bonus. O armazenamento e a
geracao de relatorios ficam em classes separadas.
OCP: novos cargos implementam sua regra de bonus sem alterar as classes
existentes.
"""


class Funcionario:
	def __init__(self, nome, salario):
		self.nome = nome
		self.salario = salario

	def calcular_bonus(self):
		raise NotImplementedError("Cada cargo deve definir seu bonus")


class Desenvolvedor(Funcionario):
	def calcular_bonus(self):
		return self.salario * 0.10


class Gerente(Funcionario):
	def calcular_bonus(self):
		return self.salario * 0.20


class Estagiario(Funcionario):
	def calcular_bonus(self):
		return self.salario * 0.05


class Analista(Funcionario):
	def calcular_bonus(self):
		return self.salario * 0.15


class FuncionarioRepository:
	def __init__(self):
		self.funcionarios = []

	def salvar(self, funcionario):
		self.funcionarios.append(funcionario)


class RelatorioFuncionarios:
	def gerar(self, funcionarios):
		for funcionario in funcionarios:
			print(
				f"Nome: {funcionario.nome} | "
				f"Salario: R$ {funcionario.salario:.2f} | "
				f"Bonus: R$ {funcionario.calcular_bonus():.2f}"
			)


funcionarios = [
	Desenvolvedor("Carlos", 5000),
	Gerente("Maria", 8000),
	Estagiario("Joao", 2000),
	Analista("Ana", 6000),
]

for funcionario in funcionarios:
	print(funcionario.calcular_bonus())

repository = FuncionarioRepository()
for funcionario in funcionarios:
	repository.salvar(funcionario)

relatorio = RelatorioFuncionarios()
relatorio.gerar(repository.funcionarios)
