from src.pipeline.classification import TextClassifier
from src.pipeline.entity_extraction import EntityExtractor
from src.pipeline.summarization import TextSummarizer

from src.schemas.analysis import AnalysisResult
from src.config.logging import setup_logger
from src.config.settings import CLASSIFICATION_LABELS


logger = setup_logger(__name__)


class TextAnalysisOrchestrator:
    def __init__(self):
        """
        Inicializa todos os componentes do pipeline de análise de texto.
        """
        self.classifier = TextClassifier(
            labels=CLASSIFICATION_LABELS
        )
        self.entity_extractor = EntityExtractor()
        self.summarizer = TextSummarizer()
    


    def run(self, text: str) -> AnalysisResult:
        """
        Executa o pipeline completo de análise de texto.
        """
        if not isinstance(text, str):
            raise TypeError("O texto de entrada deve ser uma string.")

        if not text.strip():
            raise ValueError("O texto de entrada não pode ser vazio.")
        
        
        logger.info("Iniciando pipeline de análise de texto.")

        try:
            logger.info("Executando classificação.")
            category = self.classifier.classify(text)

            logger.info("Extraindo entidades.")
            entities = self.entity_extractor.extract_entities(text)

            logger.info("Gerando resumo.")
            summary = self.summarizer.summarize(text)

        except Exception as e:

            logger.exception("Erro inesperado durante a execução do pipeline.")
            raise RuntimeError("Falha ao processar o texto.") from e

        logger.info("Pipeline finalizado com sucesso.")

        return AnalysisResult(
            category=category,
            entities=entities,
            summary=summary
        )
