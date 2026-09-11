class Profissional:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


class Servico:
    def __init__(self, descricao, valor, profissional):
        self.__descricao = descricao
        self.__valor = valor
        self.__profissional = profissional

    def get_descricao(self):
        return self.__descricao

    def get_valor(self):
        return self.__valor

    def get_profissional(self):
        return self.__profissional

    def executar(self):
        pass


class ServicoLimpeza(Servico):
    def executar(self):
        print(f"Executando serviço de limpeza. Responsável: {self.get_profissional().get_nome()}")


class ServicoManutencao(Servico):
    def executar(self):
        print(f"Executando serviço de manutenção. Responsável: {self.get_profissional().get_nome()}")


# Uso
profissional1 = Profissional("Maria")
profissional2 = Profissional("João")

servicos = [
    ServicoLimpeza("Limpeza geral", 150.0, profissional1),
    ServicoManutencao("Manutenção elétrica", 300.0, profissional2)
]

for servico in servicos:
    servico.executar()
