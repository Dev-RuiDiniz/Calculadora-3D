def calcular_orcamento(
    custo_pla: float,
    valor_maquina: float,
    custo_energia: float,
    tempo_impressao: float,
    peso_peca: float,
    percentual_lucro: float,
    depreciacao_hora: float,
    perda_material: float
) -> dict:
    """Calcula custos e retorna um dicionário com resultados."""
    custo_material = (custo_pla / 1000) * (peso_peca + perda_material)
    custo_energia_estimado = custo_energia * tempo_impressao
    custo_depreciacao = (valor_maquina * depreciacao_hora) * tempo_impressao
    custo_total = custo_material + custo_energia_estimado + custo_depreciacao
    valor_cobrar = custo_total * (1 + percentual_lucro)
    lucro = valor_cobrar - custo_total

    return {
        "custo_total": custo_total,
        "valor_cobrar": valor_cobrar,
        "lucro": lucro
    }