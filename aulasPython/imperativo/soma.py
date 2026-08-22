# Problema: Leia 5 números e mostre a soma:

soma = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    soma += numero

print(f"Soma: {soma}")