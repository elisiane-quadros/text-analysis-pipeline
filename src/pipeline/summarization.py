from transformers import pipeline


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
        result = self.summarizer(
            text,
            max_length=60,
            min_length=20,
            do_sample=False
        )

        return result[0]["summary_text"]