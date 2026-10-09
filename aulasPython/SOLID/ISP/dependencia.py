from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar_email(self, mensagem):
        pass

class EmailNotificador(Notificador):
    def enviar_email(self, mensagem):
        print(f"E-mail: {mensagem}")

class SMSNotificador(Notificador):
    def enviar_email(self, mensagem):
        print(f"SMS: {mensagem}")

class PedidoService:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador
    def finalizar(self):
        print("Pedido finalizado com sucesso!")

        self.notificador.enviar_email("Seu pedido foi finalizado com sucesso!")

email = EmailNotificador()
sms = SMSNotificador()

pedido = PedidoService(sms)
pedido.finalizar()
