class conta_bancaria():
    def __init__(self, valor):
        self.__valor = valor
    
    def getValor(self):
        return self.__valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, dinheiro):
        if dinheiro > 0:
            self.__valor += dinheiro
        else:
            self.__valor
    
cb1 = conta_bancaria(1000)
print(cb1.getValor())
cb1.setValor(1323)
print(cb1.getValor())