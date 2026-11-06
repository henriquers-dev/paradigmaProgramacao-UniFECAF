# Sistema Funcional de Processamento de Vendas.
# Importando bibliotecas necessárias
from functools import reduce


# ======================================================================
# OPERAÇÕES (funções puras: não alteram os dados e não usam print)
# ======================================================================

def filtrar_aprovados(pedidos):
    return list(filter(lambda pedido: pedido["status"] == "aprovado", pedidos))


def aplicar_desconto(pedidos, percentual):
    fator = 1 - percentual / 100
    return list(map(lambda pedido: {**pedido, "valor": pedido["valor"] * fator}, pedidos))


def calcular_faturamento(pedidos):
    return reduce(lambda total, pedido: total + pedido["valor"], pedidos, 0)


def pedidos_alto_valor(pedidos, valor_minimo):
    return list(filter(lambda pedido: pedido["valor"] > valor_minimo, pedidos))


def nomes_clientes(pedidos):
    return list(map(lambda pedido: pedido["cliente"], pedidos))


def processar(pedidos, operacao):
    return operacao(pedidos)


def gerar_dados_relatorio(pedidos, percentual_desconto=10, valor_minimo=500):
    aprovados = processar(pedidos, filtrar_aprovados)
    return {
        "total_pedidos": len(pedidos),
        "total_aprovados": len(aprovados),
        "faturamento_bruto": processar(aprovados, calcular_faturamento),
        "faturamento_com_desconto": calcular_faturamento(
            aplicar_desconto(aprovados, percentual_desconto)
        ),
        "alto_valor": pedidos_alto_valor(aprovados, valor_minimo),
        "clientes_aprovados": nomes_clientes(aprovados),
    }


# ======================================================================
# APRESENTAÇÃO (somente formatação e exibição no terminal)
# ======================================================================

def formatar_moeda(valor):
    return f"R$ {valor:.2f}"


def formatar_relatorio(dados):
    linhas_alto_valor = "\n".join(
        f"  - {p['cliente']}: {formatar_moeda(p['valor'])}" for p in dados["alto_valor"]
    )
    return (
        "===== RELATÓRIO DE VENDAS =====\n"
        f"Total de pedidos: {dados['total_pedidos']}\n"
        f"Pedidos aprovados: {dados['total_aprovados']}\n"
        f"Faturamento bruto: {formatar_moeda(dados['faturamento_bruto'])}\n"
        f"Faturamento com desconto: {formatar_moeda(dados['faturamento_com_desconto'])}\n"
        "Pedidos de alto valor:\n"
        f"{linhas_alto_valor}\n"
        "Clientes com pedidos aprovados:\n"
        f"  {', '.join(dados['clientes_aprovados'])}\n"
        "================================"
    )


def exibir_relatorio(dados):
    print(formatar_relatorio(dados))


def exibir_demonstracao(resultados):
    print("\n--- Demonstração de processar() ---")
    for descricao, resultado in resultados:
        print(f"{descricao}: {resultado}")


# ======================================================================
# EXECUÇÃO
# ======================================================================

def main():
    pedidos = [
        {"id": 1, "cliente": "Ana", "valor": 500, "status": "aprovado"},
        {"id": 2, "cliente": "Carlos", "valor": 150, "status": "pendente"},
        {"id": 3, "cliente": "Maria", "valor": 1200, "status": "aprovado"},
        {"id": 4, "cliente": "João", "valor": 80, "status": "aprovado"},
        {"id": 5, "cliente": "Fernanda", "valor": 300, "status": "cancelado"}
    ]

    # Relatório
    dados = gerar_dados_relatorio(pedidos, percentual_desconto=10, valor_minimo=500)
    exibir_relatorio(dados)

    # Demonstração da função de alta ordem com operações diferentes
    resultados = [
        ("Faturamento total (todos)", processar(pedidos, calcular_faturamento)),
        ("Clientes aprovados",
         processar(pedidos, lambda ps: nomes_clientes(filtrar_aprovados(ps)))),
        ("Faturamento com 20% de desconto",
         processar(pedidos, lambda ps: calcular_faturamento(aplicar_desconto(ps, 20)))),
    ]
    exibir_demonstracao(resultados)


if __name__ == "__main__":
    main()
