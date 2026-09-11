class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    def get_cidade(self):
        return self.__cidade

    def get_estado(self):
        return self.__estado

    def __str__(self):
        return f"{self.__cidade}/{self.__estado}"


class Hospedagem:
    def __init__(self, nome, valor_diaria):
        self.__nome = nome
        self.__valor_diaria = valor_diaria

    def get_nome(self):
        return self.__nome

    def get_valor_diaria(self):
        return self.__valor_diaria

    def reservar(self):
        pass


class Hotel(Hospedagem):
    def __init__(self, nome, valor_diaria, endereco: Endereco):
        super().__init__(nome, valor_diaria)
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco

    def reservar(self):
        print("Reserva realizada no hotel.")


class Pousada(Hospedagem):
    def __init__(self, nome, valor_diaria, endereco: Endereco):
        super().__init__(nome, valor_diaria)
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco

    def reservar(self):
        print("Reserva realizada na pousada.")


# Exemplo de uso
hospedagens = [
    Hotel("Hotel Central", 250.0, Endereco("São Paulo", "SP")),
    Pousada("Pousada do Mar", 180.0, Endereco("Búzios", "RJ"))
]

for hospedagem in hospedagens:
    hospedagem.reservar()
