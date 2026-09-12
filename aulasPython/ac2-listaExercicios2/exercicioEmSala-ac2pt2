"""
Sistema de Pagamentos — aplicando os princípios S (Single Responsibility)
e O (Open/Closed) do SOLID.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Classe base — representa apenas os dados básicos de um pagamento.
# Aplica o "S": esta classe só sabe guardar o valor do pagamento.
# ---------------------------------------------------------------------------
class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar(self):
        """Cada forma de pagamento define seu próprio processamento."""
        pass


# ---------------------------------------------------------------------------
# Formas de pagamento — cada uma com sua própria responsabilidade de
# processamento. Isso também prepara o terreno para o "O": novas formas
# de pagamento só precisam herdar de Pagamento e implementar processar().
# ---------------------------------------------------------------------------
class PagamentoPix(Pagamento):
    def processar(self):
        print(f"PIX de R$ {self.valor:.2f} processado.")


class PagamentoCartao(Pagamento):
    def processar(self):
        print(f"Pagamento no cartão de R$ {self.valor:.2f} processado.")


class PagamentoBoleto(Pagamento):
    def processar(self):
        print(f"Boleto de R$ {self.valor:.2f} gerado.")


# ---------------------------------------------------------------------------
# ComprovanteService — responsável SOMENTE pela geração do comprovante.
# ---------------------------------------------------------------------------
class ComprovanteService:
    def gerar(self, pagamento):
        print(f"Comprovante gerado no valor de R$ {pagamento.valor:.2f}")


# ---------------------------------------------------------------------------
# PagamentoRepository — responsável SOMENTE por simular o salvamento.
# ---------------------------------------------------------------------------
class PagamentoRepository:
    def salvar(self, pagamento):
        print(f"Pagamento de R$ {pagamento.valor:.2f} salvo.")


# ---------------------------------------------------------------------------
# Segunda etapa — nova forma de pagamento (PayPal), adicionada SEM alterar
# nenhuma das classes já existentes (Pix, Cartão, Boleto, ComprovanteService,
# PagamentoRepository). Isso é o princípio "O" (Open/Closed) em ação.
# ---------------------------------------------------------------------------
class PagamentoPayPal(Pagamento):
    def processar(self):
        print(f"Pagamento PayPal de R$ {self.valor:.2f} processado.")


# ---------------------------------------------------------------------------
# Exemplo de uso
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    pix = PagamentoPix(100)
    cartao = PagamentoCartao(250)
    boleto = PagamentoBoleto(500)

    pix.processar()
    cartao.processar()
    boleto.processar()

    comprovante = ComprovanteService()
    repository = PagamentoRepository()

    comprovante.gerar(pix)
    repository.salvar(pix)

    print("\n--- Segunda etapa: adicionando PayPal ---\n")

    paypal = PagamentoPayPal(300)
    paypal.processar()
    comprovante.gerar(paypal)
    repository.salvar(paypal)
