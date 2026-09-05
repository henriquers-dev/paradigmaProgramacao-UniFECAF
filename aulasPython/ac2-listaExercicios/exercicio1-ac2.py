class Instrumento():
    def __init__(self, nome, marca):
        self.__nome = nome
        self.__marca = marca

    @property
    def nome(self):
        return self.__nome

    @property
    def marca(self):
        return self.__marca

    def tocar(self):
        pass

class Musico():
    def __init__(self, nome):
        self.nome = nome

    def exibir_nome(self):
        print(f"Nome: {self.nome}")

class Violao(Instrumento):
    def __init__(self, nome, marca, dono):
        super().__init__(nome, marca)
        self.musico = Musico(dono)

    def tocar(self):
        print(f"O violão {self.nome} da marca {self.marca} está sendo tocado por {self.musico.nome}.")


class Piano(Instrumento):
    def __init__(self, nome, marca, dono):
        super().__init__(nome, marca)
        self.musico = Musico(dono)

    def tocar(self):
        print(f"O piano {self.nome} da marca {self.marca} está sendo tocado por {self.musico.nome}.")


violao = Violao("Violão Clássico", "Yamaha", "João")
piano = Piano("Piano de Cauda", "Steinway & Sons", "Maria")

violao.tocar()
piano.tocar()



