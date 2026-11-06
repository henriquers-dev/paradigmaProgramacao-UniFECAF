# MAP()
# map(funcao, iteravel)

precos = [100, 200, 300, 400]

def aplicar_aumento(preco):
    return preco * 1.1

novos_precos = list(map(lambda preco: preco * 1.1, precos))
print(novos_precos)


# FILTER()
# filter(funcao, iteravel)

produtos = [
    {'nome': 'fone de ouvido sem fio', 'preco': 1020},
    {'nome': 'mouse', 'preco': 140},
    {'nome': 'teclado', 'preco': 1200},
    {'nome': 'monitor', 'preco': 800}
]

promocao = list(
    filter(
        lambda produto: produto['preco'] > 1000, produtos
    )
)

print(promocao)


# REDUCE()
# reduce(funcao, iteravel)

valores = [100, 200, 50, 150]

total = reduce(lambda acum, valor: acum + valor, valores)
print(total)
