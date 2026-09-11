# 1 - S (Single Responsability Principle) Princípio de Responsabilidade Única


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class CalcularMedia:
    def calcular_media(self, aluno):
        return aluno.nota

class AlunoRepository:
    def salvar_aluno(self, aluno):
        print(f"Salvando o nome {aluno.nome}")

class EmailService:
    def enviar_email(self, aluno):
        print(f"Enviando email para {aluno.nome}")

aluno = Aluno("Pedro", 8.5)
media = CalcularMedia()
bd = AlunoRepository()
email = EmailService()

print(media.calcular_media(aluno))
media.calcular_media(aluno)
bd.salvar_aluno(aluno)
email.enviar_email(aluno)
