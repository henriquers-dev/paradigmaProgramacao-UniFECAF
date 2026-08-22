"""
    TRANSFORMAR O ALGORITMO EM FUNÇÃO
"""

def calcular_media(n1, n2):
    return(n1 + n2) / 2

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = calcular_media(nota1, nota2)

if media >= 6:
    print("Aprovado")

elif(media >= 3.5 and media < 6):
    print("Exame")

else:
    print("Reprovado")