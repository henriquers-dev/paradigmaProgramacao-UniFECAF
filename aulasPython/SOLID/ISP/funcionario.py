from abc import ABC, abstractmethod

class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Programavel(ABC):
    @abstractmethod
    def programar(self):
        pass

class Dirigivel(ABC):
    @abstractmethod
    def dirigir(self):
        pass

class Funcionario(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

    @abstractmethod
    def dirigir(self):
        pass

    @abstractmethod
    def programar(self):
        pass


class Programador(Trabalhador, Programavel):
    def trabalhar(self):
        print("O programador está trabalhando.")

    def programar(self):
        print("O programador está programando.")

class Motorista(Trabalhador, Dirigivel):
    def trabalhar(self):
        print("O motorista está trabalhando.")

    def dirigir(self):
        print("O motorista está dirigindo.")
