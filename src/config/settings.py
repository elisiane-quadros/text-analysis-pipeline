"""
Configurações globais do pipeline de análise de texto.
"""

# Labels usadas na classificação zero-shot
CLASSIFICATION_LABELS = [
    "Notícia",
    "Blog",
    "Artigo acadêmico",
    "Outro"
]

# Configurações de sumarização
SUMMARIZATION_CONFIG = {
    "max_length": 60,
    "min_length": 20,
    "do_sample": False
}

