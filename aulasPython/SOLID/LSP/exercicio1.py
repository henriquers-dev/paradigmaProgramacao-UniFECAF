class Pagamento:
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor}")

class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Pix de R$ {valor}")


class Cartao(Pagamento):
    def pagar(self, valor):
        print(f"Cartão de R$ {valor}")

class Dinheiro(Pagamento):
    def pagar(self, valor):
        raise Exception("Não suportado.")

def finalizar_pagamento(pagamento, valor):
    pagamento.pagar(valor)

pix = Pix()
cartao = Cartao()
dinheiro = Dinheiro()

finalizar_pagamento(pix, 200)
finalizar_pagamento(cartao, 200)
finalizar_pagamento(dinheiro, 200)
