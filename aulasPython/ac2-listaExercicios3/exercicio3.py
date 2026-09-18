from abc import ABC, abstractmethod


class Funcionario(ABC):
	def __init__(self, nome, salario):
		self.nome = nome
		self.salario = salario

	@abstractmethod
	def calcular_bonus(self):
		pass


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

	def listar(self):
		return self.funcionarios.copy()


class RelatorioFuncionarios:
	def gerar(self, funcionarios):
		for funcionario in funcionarios:
			bonus = funcionario.calcular_bonus()
			print(
				f"{funcionario.nome} - Salario: R$ {funcionario.salario:.2f} "
				f"- Bonus: R$ {bonus:.2f}"
			)


def main():
	funcionarios = [
		Desenvolvedor("Carlos", 5000),
		Gerente("Maria", 8000),
		Estagiario("João", 2000),
		Analista("Ana", 6000),
	]

	repository = FuncionarioRepository()
	for funcionario in funcionarios:
		repository.salvar(funcionario)

	relatorio = RelatorioFuncionarios()
	relatorio.gerar(repository.listar())


if __name__ == "__main__":
	main()
