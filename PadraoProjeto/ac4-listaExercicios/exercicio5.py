from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================
# MODELS
# ============================================================
class Produto:
    def __init__(self, codigo, nome, preco):
        self.__codigo = codigo
        self.__nome = nome
        self.preco = preco  # passa pelo setter (validação)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor is None or valor <= 0:
            raise ValueError("O preço do produto deve ser positivo.")
        self.__preco = float(valor)


class Pedido:
    """Pedido + Subject do padrão Observer."""

    def __init__(self, numero, cliente, produtos, endereco=None, observacao=None):
        self.__numero = numero
        self.__cliente = cliente
        self.__produtos = list(produtos)
        self.__endereco = endereco
        self.__observacao = observacao
        self.__confirmado = False
        self.__observadores = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def produtos(self):
        return list(self.__produtos)

    @property
    def endereco(self):
        return self.__endereco

    @property
    def observacao(self):
        return self.__observacao

    @property
    def confirmado(self):
        return self.__confirmado

    def total(self):
        return sum(p.preco for p in self.__produtos)

    def confirmar(self):
        if self.__confirmado:
            raise RuntimeError(f"Pedido {self.__numero} já foi confirmado.")
        self.__confirmado = True

    # --- Observer (Subject) ---
    def adicionar_observador(self, observador):
        if observador not in self.__observadores:
            self.__observadores.append(observador)

    def remover_observador(self, observador):
        if observador in self.__observadores:
            self.__observadores.remove(observador)

    def notificar(self, mensagem):
        for observador in self.__observadores:
            observador.atualizar(mensagem)


# ============================================================
# BUILDER
# ============================================================
class PedidoBuilder:
    def __init__(self):
        self._numero = None
        self._cliente = None
        self._produtos = []
        self._endereco = None
        self._observacao = None

    def numero(self, numero):
        self._numero = numero
        return self

    def cliente(self, cliente):
        self._cliente = cliente
        return self

    def adicionar_produto(self, produto):
        self._produtos.append(produto)
        return self

    def endereco(self, endereco):
        self._endereco = endereco
        return self

    def observacao(self, observacao):
        self._observacao = observacao
        return self

    def build(self):
        if self._numero is None:
            raise ValueError("O pedido precisa ter um número.")
        if not self._cliente:
            raise ValueError("O pedido precisa ter um cliente.")
        if not self._produtos:
            raise ValueError("O pedido precisa ter pelo menos um produto.")
        return Pedido(self._numero, self._cliente, self._produtos,
                      self._endereco, self._observacao)


# ============================================================
# PAGAMENTOS (ADAPTER)
# ============================================================
class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


# --- Gateways externos simulados (interfaces incompatíveis) ---
class GatewayPix:
    def transferir(self, quantia):
        print(f"Pix realizado: R$ {quantia:.2f}")
        return True


class GatewayCartao:
    def cobrar_cartao(self, total):
        print(f"Cartão aprovado: R$ {total:.2f}")
        return True


class GatewayBoleto:  # Desafio A
    def emitir_boleto(self, valor):
        print(f"Boleto emitido e compensado: R$ {valor:.2f}")
        return True


# --- Adapters ---
class PixAdapter(Pagamento):
    def __init__(self, gateway=None):
        self._gateway = gateway or GatewayPix()

    def pagar(self, valor):
        try:
            return bool(self._gateway.transferir(valor))
        except Exception:
            return False


class CartaoAdapter(Pagamento):
    def __init__(self, gateway=None):
        self._gateway = gateway or GatewayCartao()

    def pagar(self, valor):
        try:
            return bool(self._gateway.cobrar_cartao(valor))
        except Exception:
            return False


class BoletoAdapter(Pagamento):  # Desafio A
    def __init__(self, gateway=None):
        self._gateway = gateway or GatewayBoleto()

    def pagar(self, valor):
        try:
            return bool(self._gateway.emitir_boleto(valor))
        except Exception:
            return False


# ============================================================
# OBSERVERS
# ============================================================
class PedidoObserver(ABC):
    @abstractmethod
    def atualizar(self, mensagem):
        """Recebe um dict com: numero, cliente, total."""
        pass


class EmailObserver(PedidoObserver):
    def atualizar(self, mensagem):
        print("EMAIL:")
        print(f"  {mensagem['cliente']}, seu pedido foi confirmado.")


class EstoqueObserver(PedidoObserver):
    def atualizar(self, mensagem):
        print("ESTOQUE:")
        print(f"  Separar os produtos do pedido {mensagem['numero']}.")


class FinanceiroObserver(PedidoObserver):
    def atualizar(self, mensagem):
        print("FINANCEIRO:")
        print(f"  Pagamento de R$ {mensagem['total']:.2f} registrado.")


class LogObserver(PedidoObserver):  # Desafio B
    def __init__(self, arquivo="log_pedidos.txt"):
        self._arquivo = arquivo

    def atualizar(self, mensagem):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self._arquivo, "a", encoding="utf-8") as f:
            f.write(f"[{agora}] Pedido {mensagem['numero']} confirmado | "
                    f"Cliente: {mensagem['cliente']} | "
                    f"Total: R$ {mensagem['total']:.2f}\n")


# ============================================================
# SERVIÇO
# ============================================================
class FinalizadorPedido:
    """Depende apenas da abstração Pagamento (DIP)."""

    def finalizar(self, pedido, pagamento: Pagamento):
        # Desafio C: impede pagamento duplicado
        if pedido.confirmado:
            print(f"Pedido {pedido.numero} já confirmado. Pagamento não será repetido.")
            return False

        total = pedido.total()
        print("Processando pagamento...")

        if not pagamento.pagar(total):
            print("Pagamento recusado! Pedido não confirmado.")
            return False

        print("Pagamento aprovado!")
        pedido.confirmar()
        print(f"Pedido {pedido.numero} confirmado!")

        print("\n========== NOTIFICAÇÕES ==========")
        pedido.notificar({"numero": pedido.numero,
                          "cliente": pedido.cliente,
                          "total": total})
        return True


# ============================================================
# MAIN
# ============================================================
def main():
    produto1 = Produto(1, "Teclado Mecânico", 250.00)
    produto2 = Produto(2, "Mouse Gamer", 150.00)

    pedido = (
        PedidoBuilder()
        .numero(1001)
        .cliente("Maria")
        .adicionar_produto(produto1)
        .adicionar_produto(produto2)
        .endereco("Rua das Flores, 100")
        .observacao("Entregar pela manhã")
        .build()
    )

    for obs in (EmailObserver(), EstoqueObserver(), FinanceiroObserver(), LogObserver()):
        pedido.adicionar_observador(obs)

    formas = {"PIX": PixAdapter, "CARTÃO": CartaoAdapter, "BOLETO": BoletoAdapter}
    forma = "PIX"  # troque para "CARTÃO" ou "BOLETO"

    print("========== LOJA VIRTUAL ==========")
    print(f"Cliente: {pedido.cliente}")
    print(f"Pedido: {pedido.numero}")
    print("Produtos:")
    for p in pedido.produtos:
        print(f"- {p.nome}: R$ {p.preco:.2f}")
    print(f"Total: R$ {pedido.total():.2f}")
    print(f"Forma de pagamento: {forma}\n")

    finalizador = FinalizadorPedido()
    finalizador.finalizar(pedido, formas[forma]())

    # Desafio C: tentativa de pagar novamente
    print("\n--- Tentando pagar o mesmo pedido de novo ---")
    finalizador.finalizar(pedido, PixAdapter())

    print("\n========== FINALIZADO ==========")


if __name__ == "__main__":
    main()
