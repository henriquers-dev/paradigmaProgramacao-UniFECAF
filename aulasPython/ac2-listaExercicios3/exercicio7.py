from abc import ABC, abstractmethod


class Conta(ABC):
	def __init__(self, saldo):
		self.saldo = saldo


class ContaComDeposito(Conta):
	def depositar(self, valor):
		self.saldo += valor


class ContaSacavel(ContaComDeposito, ABC):
	@abstractmethod
	def sacar(self, valor):
		pass


class ContaCorrente(ContaSacavel):
	def sacar(self, valor):
		self.saldo -= valor


class ContaInvestimento(ContaComDeposito):
	def investir(self, valor):
		self.saldo += valor


def realizar_deposito(conta, valor):
	conta.depositar(valor)
	print(f"Depósito de {valor} realizado!")


def realizar_saque(conta, valor):
	conta.sacar(valor)
	print(f"Saque de {valor} realizado!")


def realizar_investimento(conta, valor):
	conta.investir(valor)
	print(f"Investimento de {valor} realizado!")


conta_corrente = ContaCorrente(1000)
realizar_deposito(conta_corrente, 100)
realizar_saque(conta_corrente, 200)
print(f"Saldo da conta corrente: {conta_corrente.saldo}")

conta_investimento = ContaInvestimento(1000)
realizar_deposito(conta_investimento, 500)
realizar_investimento(conta_investimento, 200)
print(f"Saldo da conta de investimento: {conta_investimento.saldo}")
