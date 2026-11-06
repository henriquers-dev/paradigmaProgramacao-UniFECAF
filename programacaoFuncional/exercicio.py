from functools import reduce

vendas = [50, 150, 200, 300, 100, 80]

filtradas = filter(
    lambda valor: valor > 100, 
    vendas
)

print(f"Valores filtrados: {list(filtradas)}")
com_taxa = map(
    lambda valor: valor * 1.05,
    filtradas
)

total = reduce(
    lambda acum, valor: 
    acum + valor,com_taxa,
    0
)

print(f"Total das vendas com taxa: R$ {total:.2f}")
