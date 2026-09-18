class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def calcular_total(self):
        return self.valor * 1.10

class PedidoRepository:
    def salvar(self, pedido):
        print("Salvando pedido no banco de dados...")

class EmailService:
    def enviar_confirmacao(self, pedido):
        print(f"Enviando confirmação para {pedido.cliente}...")

def main():
    pedido = Pedido("Henrique", 50)
    repository = PedidoRepository()
    email_service = EmailService()

    total = pedido.calcular_total()
    print(f"Total do pedido: R$ {total:.2f}")
    repository.salvar(pedido)
    email_service.enviar_confirmacao(pedido)


if __name__ == "__main__":
    main()
