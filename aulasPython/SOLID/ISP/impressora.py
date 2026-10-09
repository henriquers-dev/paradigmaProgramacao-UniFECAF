from abc import ABC, abstractmethod


class Basica(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Multifuncional(ABC):
    @abstractmethod
    def escanear(self):
        pass

    @abstractmethod
    def enviarFAX(self):
        pass


class ImpressoraBasica(Basica):
    def imprimir(self):
        print("A impressora básica está imprimindo.")


class ImpressoraMultifuncional(Basica, Multifuncional):
    def imprimir(self):
        print("A impressora multifuncional está imprimindo.")

    def escanear(self):
        print("A impressora multifuncional está escaneando.")

    def enviarFAX(self):
        print("A impressora multifuncional está enviando fax.")


basica = ImpressoraBasica()
multifuncional = ImpressoraMultifuncional()

basica.imprimir()
multifuncional.imprimir()
multifuncional.escanear()
multifuncional.enviarFAX()

print(basica.__class__.__name__)  # Saída: ImpressoraBasica
print(multifuncional.__class__.__name__)  # Saída: ImpressoraMultifuncional
