def verificar_senha(senha_inserida: str) -> bool:
    """Verifica se a senha está correta."""
    senha_correta = "1234"  # Em produção, use hash!
    return senha_inserida == senha_correta