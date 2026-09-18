from abc import ABC, abstractmethod


class Ave:
	"""Representa qualquer ave, independentemente de ela voar ou nao."""

	def comer(self):
		print("A ave está comendo.")


class AveQueVoa(Ave, ABC):
	@abstractmethod
	def voar(self):
		pass


class Aguia(AveQueVoa):
	def voar(self):
		print("A águia está voando.")


class Pardal(AveQueVoa):
	def voar(self):
		print("O pardal está voando.")


class Pinguim(Ave):
	pass


aves = [Aguia(), Pardal(), Pinguim()]

for ave in aves:
	ave.comer()

aves_que_voam = [Aguia(), Pardal()]
for ave in aves_que_voam:
	ave.voar()
