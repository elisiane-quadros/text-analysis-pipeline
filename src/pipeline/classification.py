from transformers import pipeline
from typing import List

class TextClassifier:
    """Classificador de texto usando zero-shot classification."""

    def __init__(self, labels: List[str]):
        self.labels = labels
        self.classifier = pipeline(
            task="zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        
    
    def classify(self, text: str) -> str:
        """Classifica um texto em uma das categorias definidas."""

        result = self.classifier(text, self.labels)
        return result["labels"][0]