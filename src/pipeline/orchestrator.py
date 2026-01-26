from src.pipeline.classification import TextClassifier
from src.pipeline.ner import EntityExtractor
from src.pipeline.summarization import TextSummarizer


class TextAnalysisOrchestrator:
    def __init__(self):
        """
        Inicializa todos os componentes do pipeline de análise de texto.
        """
        self.classifier = TextClassifier(
            labels=["Notícia", "Blog", "Artigo acadêmico", "Outro"]
        )
        self.entity_extractor = EntityExtractor()
        self.summarizer = TextSummarizer()
    

    def run(self, text: str) -> dict:
        """
        Executa o pipeline completo de análise de texto.
        """
        category = self.classifier.classify(text)
        entities = self.entity_extractor.extract_entities(text)
        summary = self.summarizer.summarize(text)

        return {
            "category": category,
            "entities": entities,
            "summary": summary
        }