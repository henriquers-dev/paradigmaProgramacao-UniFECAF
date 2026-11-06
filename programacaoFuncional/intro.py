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
