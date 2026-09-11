class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_salario(self):
        print("Calculando salário do funcionário...")

    def salvar_banco(self):
        print(f"Salvando funcionário {self.nome}")
    
    def enviar_email(self):
        print(f"Enviando email para {self.nome}")
