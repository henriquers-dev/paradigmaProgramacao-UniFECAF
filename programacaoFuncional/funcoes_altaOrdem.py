# MAP()
# map(funcao, iteravel)

precos = [100, 200, 300, 400]

def aplicar_aumento(preco):
    return preco * 1.1

novos_precos = list(map(aplicar_aumento, precos))
print(novos_precos)
