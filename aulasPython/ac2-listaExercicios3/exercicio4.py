"""
Exemplo do Open/Closed Principle (OCP).

Problema da implementação original: a classe Notificacao precisava ser
alterada sempre que um novo tipo de envio era adicionado. Isso viola o OCP,
pois a classe não estava fechada para modificacao.
"""


class Email:
	def enviar(self, mensagem):
		print(f"Enviando EMAIL: {mensagem}")


class SMS:
	def enviar(self, mensagem):
		print(f"Enviando SMS: {mensagem}")


class WhatsApp:
	def enviar(self, mensagem):
		print(f"Enviando WhatsApp: {mensagem}")


class PushNotification:
	def enviar(self, mensagem):
		print(f"Enviando PUSH: {mensagem}")


def enviar_notificacao(notificador, mensagem):
	notificador.enviar(mensagem)


email = Email()
sms = SMS()
whatsapp = WhatsApp()
push = PushNotification()

enviar_notificacao(email, "Pedido realizado!")
enviar_notificacao(sms, "Pagamento aprovado!")
enviar_notificacao(whatsapp, "Seu pedido foi enviado!")
enviar_notificacao(push, "Voce recebeu uma nova mensagem!")
