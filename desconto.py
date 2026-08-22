def calcular_desconto(valor, percentual):
    desconto = valor * percentual / 100
    return valor - desconto
    """
        PEGAR VALOR E APLICAR O DESCONTO
        Ex.: desconto de 10%
        Resultado: ??
    """

valor = float(input("Valor: "))
percentual = float(input("Desconto: "))
valor_final = calcular_desconto(valor, percentual)
print("O valor final é de ", valor_final)