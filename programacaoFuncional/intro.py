numeros = [1, 2, 3, 4, 5, 6]
dobrados = []


for item in numeros:
    dobrados.append(item * 2)

print(dobrados)


# FUNÇÕES
dobrados = list(map(lambda n:n*2, numeros))
print(dobrados)


# FUNÇÕES PURAS:
def calcular_desconto(valor, percentual):
    return valor - (valor * percentual / 100)

print(calcular_desconto(220, 20)) # 176.0


# FUNÇÕES IMPURAS:
desconto = 10
def calcular_desconto2(valor):
    return valor - (valor * desconto / 100)

print(calcular_desconto2(220)) # 198.0


# FUNÇÕES DE ALTA ORDEM:
# FUNÇÃO COMO VALOR:
def saudacao(nome):
    return f'Olá {nome}'

mensagem = saudacao
print(mensagem('HENRIQUE')) # Olá HENRIQUE


# NOVO EXEMPLO DE FUNÇÃO DE ALTA ORDEM:
def calcular(a, b, operacao):
    return operacao(a, b)

def somar(a, b):
    return a + b
def multiplicar(a, b):
    return a * b
def subtrair(a, b):
    return a - b
print(calcular(10, 5, somar)) # 15
print(calcular(10, 5, multiplicar)) # 50
print(calcular(10, 5, subtrair)) # 5

# EXPRESSÃO LAMBDA:
def quadrado(numero):
    return numero ** 2

print("Sem lambda: ", quadrado(5))
quadrado_lambda = lambda numero: numero ** 2
print(f"Com lambda: {quadrado_lambda(5)}")


# USO APLICÁVEL DE LAMBDA:
def executar_operacao(a, b, operacao):
    return operacao(a, b)

resultado = executar_operacao(10, 5, lambda x, y: x + y)
print(f"Resultado da operação: {resultado}")
