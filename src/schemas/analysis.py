from pydantic import BaseModel
from typing import List, Dict

class AnalysisResult(BaseModel):
    """
    Define o formato final do resultado da análise de texto.
    Esse schema garante que a saída do pipeline seja previsível,
    validada e documentada.
    """

    category: str
    entities: Dict[str, List[str]]
    summary: str
