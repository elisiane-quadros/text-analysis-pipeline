from transformers import pipeline
from src.config.settings import SUMMARIZATION_CONFIG


class TextSummarizer:
    def __init__(self):
        """
        Inicializa o pipeline de sumarização de texto.
        """
        self.summarizer = pipeline(
            task="summarization",
            model="facebook/bart-large-cnn"
        )

    def summarize(self, text: str) -> str:
        """
        Recebe um texto e retorna um resumo curto.
        """
        text_length = len(text.split())

        if text_length < 30:
            return text

        max_length = min(
            SUMMARIZATION_CONFIG["max_length"],
            max(10, text_length)
        )

        min_length = min(
            SUMMARIZATION_CONFIG["min_length"],
            max(text_length // 2)
        )

        result = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=SUMMARIZATION_CONFIG["do_sample"]
        )

        return result[0]["summary_text"]